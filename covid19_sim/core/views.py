from flask import render_template, Blueprint

core = Blueprint('core',__name__)

@core.route("/")
def index():
    return render_template("index.html"),200

@core.route("/about")
def about():
    return render_template("about.html"),200

@core.route("/links")
def links():
    return render_template("links.html"),200