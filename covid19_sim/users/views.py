from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

from werkzeug.security import generate_password_hash,check_password_hash

from covid19_sim import db
from covid19_sim.db_models import User
from covid19_sim.users.forms import RegistrationForm, LoginForm
# from covid19_sim.users.picture_handler import add_profile_pic


users = Blueprint('users', __name__)


#################################################

@users.route('/register', methods=['GET','POST'])
def register():
    already_exists = False
    if request.method == 'POST':
        # print('/register:  request: ',request)
        form = RegistrationForm(request).parsed()
        # print('/register:  form: ',form)
        existing_user = User.query.filter_by(email=form.get('email')).first()
        # print('/register:  existing_user: ',existing_user)
        form_complete = all(val for val in form.values())
        if not existing_user and form_complete:
            user = User(**form).save()
            return redirect("/login")
        else:
            already_exists = True
    return render_template('register.html',already_exists=already_exists)

@users.route('/login', methods=['GET', 'POST'])
def login():
    login_fail_msg = None
    if request.method == 'POST':
        form = LoginForm(request).parsed()
        print('/login/form: ',form)
        if all(val for val in form.values()):
            user = User.query.filter_by(email=form.get('email')).first()
            if user:
                if user.check_password(form.get('password')):
                    login_user(user)
                    flash('Logged in successfully.')
                    next = request.args.get('next')
                    if not next:
                        next = "/run"
                    return redirect(next)
                else:
                    login_fail_msg = "Sorry, email and password do not match."
            else:
                login_fail_msg = "Sorry, email not registerd."
                print(login_fail_msg)
    return render_template("login.html",login_fail_msg=login_fail_msg)

@users.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect("/")


# @users.route("/account", methods=['GET', 'POST'])
# @login_required
# def account():

#     form = UpdateUserForm()

#     if form.validate_on_submit():
#         print(form)
#         if form.picture:
#             username = current_user.username
#             pic = add_profile_pic(form.picture,username)
#             current_user.profile_image = pic

#         current_user.username = form.username
#         current_user.email = form.email
#         db.session.commit()
#         flash('User Account Updated')
#         return redirect(url_for('users.account'))

#     elif request.method == 'GET':
#         form.username = current_user.username
#         form.email = current_user.email

#     profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)
#     return render_template('account.html', profile_image=profile_image, form=form)


# @users.route("/<username>")
# def user_posts(username):
#     page = request.args.get('page', 1, type=int)
#     user = User.query.filter_by(username=username).first_or_404()
#     blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
#     return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)
