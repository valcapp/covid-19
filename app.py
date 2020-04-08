from flask import Flask, request, render_template, url_for
import pysd


app = Flask(__name__)

from flask_restful import Api
from resources.scenario import Scenario
api = Api(app)
api.add_resource(Scenario,'/scenario/<string:run_name>')

model = pysd.read_vensim('sd/community corona 8.mdl')
import numpy as np
config = {
    'return_columns':['TIME','Susceptible','Infected','Deaths','Recovered'],
    'return_timestamps':np.arange(0, 300, 2).tolist()
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run")
def run():
    params = {
        'Behavioral Risk Reduction':0,
        'Potential Isolation Effectiveness':0
    }
    data = {
        'Behavioral Risk Reduction':request.args.get('Behavioral Risk Reduction'),
        'Potential Isolation Effectiveness':request.args.get('Potential Isolation Effectiveness')
    }
    new_params = dict((key,float(par)) for key,par in data.items() if par)
    params.update(new_params)
    config.update({'params':params})
    run = model.run(**config).to_json()
    # return run
    return render_template('run.html',run=run,params=params)


app.config['DEBUG'] = True

if __name__ == "__main__":
    if app.config['DEBUG']:
        app.run(debug=True,port=5000)
    else:
        app.run(port=5000)