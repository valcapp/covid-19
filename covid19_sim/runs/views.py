from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

from covid19_sim.sd import sd_run
import json

from covid19_sim import db
from covid19_sim.db_models import Run
from covid19_sim.runs.forms import RunForm, SaveRunForm

runs = Blueprint('runs',__name__)

@runs.route("/run")
def run():
    form = RunForm(request).parsed()
    data = sd_run(form)
    return render_template('run.html',**data),200

def dump_if_dict(value):
    if type(value) is dict:
        return json.dumps(value)
    else:
        return value

@runs.route("/saverun",methods=['POST'])
@login_required
def saverun():
    form = SaveRunForm(request).parsed()
    run_name = form.get('name')
    if run_name:
        data = sd_run(form)
        json_data = dict((key,dump_if_dict(value)) for key,value in data.items())
        Run(current_user.id,run_name,**json_data).save()
        # try using flash messages, bootstrap modals and redirect to run page
        return redirect('/compare')
    return {"message":"Error Occurred"},500

@runs.route("/compare")
@login_required
def compare():
    run_models = Run.query.filter_by(user_id=current_user.id)
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

@runs.route("/listruns")
@login_required
def list_runs():
    runs = Run.query.filter_by(user_id=current_user.id)
    runs_dict = {'runs':[run.json() for run in runs]}
    return json.dumps(runs_dict)

@runs.route("/manage")
@login_required
def manage():
    runs = Run.query.filter_by(user_id=current_user.id)
    # runs_dict = {'runs':[run.json() for run in runs]}
    runs = [run.json() for run in runs]
    return render_template("manage.html",runs=runs),200

@runs.route("/<int:run_id>/update",methods=['POST'])
@login_required
def update(run_id):
    run = Run.query.filter_by(id=run_id).first()
    form = SaveRunForm(request).parsed()
    run_name = form.get('name')
    data = sd_run(form)
    json_data = dict((key,dump_if_dict(value)) for key,value in data.items())
    run.update(run_name,**json_data)
    return redirect("/manage")

@runs.route("/<int:run_id>/delete",methods=['POST'])
@login_required
def delete(run_id):
    run = Run.query.filter_by(id=run_id).first()
    run.delete()
    return redirect("/manage")
