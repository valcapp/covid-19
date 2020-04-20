import os
import json

from sd.model import sd_run

from flask import Flask, request, render_template, url_for, redirect, jsonify

app = Flask(__name__)
app.config['SECRET_KEY']='covid-19'

#########################
##### SQL DATABASE ######
#########################
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app) #
from db import db
db.init_app(app)
from flask_migrate import Migrate
Migrate(app,db)


#########################
##### DB MODELS #########
#########################
from db_models import Run
from forms import RunForm, SaveRunForm


#########################
############## VIEWS ####
#########################
runs = {}

@app.route("/")
def index():
    return render_template("index.html"),200

@app.route("/run")
def run():
    form = RunForm(request).parsed()
    print('/run: form is: ',form)
    data = sd_run(form)
    return render_template('run.html',**data),200

def dump_if_dict(value):
    if type(value) is dict:
        return json.dumps(value)
    else:
        return value

@app.route("/saverun",methods=['POST'])
def saverun():
    form = SaveRunForm(request).parsed()
    # print('/saverun: form is: ',form)
    run_name = form.get('name')
    if run_name:
        # print('selected_time from form_data: ',form['selected_time'])
        data = sd_run(form)
        # print('selected_time from run_data: ',run_data['selected_time'])
        json_data = dict((key,dump_if_dict(value)) for key,value in data.items())
        # print('selected_time from json_data: ',json_data['selected_time'])
        Run(run_name,**json_data).save()
        return redirect(url_for('compare'))
    return {"message":"Error Occurred"},500
    
@app.route("/compare")
def compare():
    run_models = Run.query.all()
    runs_dict = {'runs':dict((run.name, run.json()) for run in run_models if run.results)}
    # print('From the app: ',runs_dict['runs'].keys())
    # return json.dumps(runs_dict)
    run_names = list(runs_dict['runs'].keys())
    if len(run_names)>0:
        runs = json.dumps(runs_dict)
    else:
        runs = None
    return render_template("compare.html",runs=runs, run_names = run_names),200
    # return render_template("compare.html",runs_dict=runs_dict,runs_json=json.dumps(runs_dict)),200

@app.route("/listruns")
def list_runs():
    runs = Run.query.all()
    runs_dict = {'runs':[run.json() for run in runs]}
    return json.dumps(runs_dict)

@app.route("/manage")
def manage():
    runs = Run.query.all()
    # runs_dict = {'runs':[run.json() for run in runs]}
    runs = [run.json() for run in runs]
    return render_template("manage.html",runs=runs),200

@app.route("/<int:run_id>/update",methods=['POST'])
def update(run_id):
    run = Run.find_by_id(run_id)
    form = SaveRunForm(request).parsed()
    run_name = form.get('name')
    data = sd_run(form)
    json_data = dict((key,dump_if_dict(value)) for key,value in data.items())
    run.update(run_name,**json_data)
    return redirect("/manage")

@app.route("/<int:run_id>/delete",methods=['POST'])
def delete(run_id):
    run = Run.find_by_id(run_id)
    run.delete()
    return redirect("/manage")

@app.route("/links")
def links():
    return render_template("links.html"),200


app.config['DEBUG'] = True

if __name__ == "__main__":
    app.run(
        debug = app.config['DEBUG'],
        port = 5000
    )
