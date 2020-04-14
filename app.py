from flask import Flask, request, render_template, url_for, redirect
import pysd
import json


app = Flask(__name__)

from flask_restful import Api
from resources.scenario import Scenario
api = Api(app)
api.add_resource(Scenario,'/scenario/<string:run_name>')

model = pysd.read_vensim('sd/community corona 8.mdl')
import numpy as np

runs = {}

config = {
    'return_columns':['TIME','Susceptible','Exposed','Infected','Deaths','Recovered'],
    'return_timestamps':np.arange(0, 300, 2).tolist()
}

default_params = {
    'Behavioral Risk Reduction':0,
    'Potential Isolation Effectiveness':0
}

def get_run_data(request):
    params = default_params.copy()
    data = {
        'Behavioral Risk Reduction':request.values.get('Behavioral Risk Reduction'),
        'Potential Isolation Effectiveness':request.values.get('Potential Isolation Effectiveness')
    }
    print(data)
    new_params = dict((key,float(par)) for key,par in data.items() if par)
    params.update(new_params)
        
    run = model.run(**config,params=params).to_json()
        
    selected_time = request.values.get('selectedTime')
    if not selected_time:
        selected_time = 40
        
    return {
        'params':params,
        'run':run,
        'selected_time':selected_time
    }

@app.route("/")
def index():
    return render_template("index.html"),200

@app.route("/run")
def run():
    run_data = get_run_data(request)
    # print(run_data)
    return render_template('run.html',**run_data),200

@app.route("/saverun",methods=['POST'])
def saverun():
    run_name = request.form.get('run_name')
    run_data = get_run_data(request)
    # print( {
    #     'Behavioral Risk Reduction':request.args.get('Behavioral Risk Reduction'),
    #     'Potential Isolation Effectiveness':request.args.get('Potential Isolation Effectiveness')
    # } )
    # print(run_data)
    # print(run_name)
    if run_name:
        runs[run_name]=run_data
        return redirect('/compare'),201
    return {"message":"Error Occurred"},500
    

@app.route("/compare")
def compare():
    return render_template("compare.html",runs=json.dumps(runs),run_names=list(runs.keys())),200


@app.route("/links")
def links():
    return render_template("links.html"),200

app.config['DEBUG'] = True

if __name__ == "__main__":
    if app.config['DEBUG']:
        app.run(debug=True,port=5000)
    else:
        app.run(port=5000)