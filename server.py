from flask import Flask, request, make_response, render_template, redirect, flash, url_for
from flask.ext.login import LoginManager, login_user, logout_user, login_required
from flask.ext.bcrypt import check_password_hash
import forms
import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'


app = Flask(__name__)
app.secret_key = 'futeba_app'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'index'


@login_manager.user_loader
def load_user(user_id):
  try:
    return models.User.objects(id=user_id).get()
  except models.DoesNotExist:
    return None

@app.route("/", methods=('GET', 'POST'))
def index():
    login_form = forms.LoginForm()
    # Login
    if login_form.validate_on_submit():
        if login_form.login_type.data == 'user':
            try:
                user = models.User.objects(email=login_form.email.data).get()
            except models.DoesNotExist:
                flash("Your email or password doesn't match!", "error")
            else:
                if check_password_hash(user.password, login_form.password.data):
                    login_user(user)
                    flash("You've benn logged in!", "success")
                    return redirect(url_for('home'))
                else:
                    flash("Your email or password doesn't match!", "error")
        else:
            try:
                user = models.Place.objects(email=login_form.email.data).get()
            except models.DoesNotExist:
                flash("Your email or password doesn't match!", "error")
            else:
                if check_password_hash(user.password, login_form.password.data):
                    login_user(user)
                    flash("You've benn logged in!", "success")
                    return redirect(url_for('home'))
                else:
                    flash("Your email or password doesn't match!", "error")
    return make_response(render_template('login.html', login_form=login_form))


@app.route("/new_user", methods=('GET', 'POST'))
def new_user():
    user_form = forms.RegisterFormUser()
    # Register User
    if user_form.validate_on_submit():
        flash("Registered!", "success")
        models.User.create_user(
            username = user_form.username.data,
            bday = user_form.bday.data,
            genre = user_form.genre.data,
            address = user_form.address.data,
            city = user_form.city.data,
            state = user_form.state.data,
            email = user_form.email.data,
            password = user_form.password.data
        )
        user = models.User.objects(email=user_form.email.data).get()
        login_user(user)
        return redirect(url_for('home'))
    return make_response(render_template('new_user.html', user_form=user_form))


@app.route("/new_place", methods=('GET', 'POST'))
def new_place():
    place_form = forms.RegisterFormPlace()
    # Register Place
    if place_form.validate_on_submit():
        flash("Registered!", "success")
        models.Place.create_place(
            name = place_form.name.data,
            address = place_form.address.data,
            city = place_form.city.data,
            state = place_form.state.data,
            sport = place_form.sport.data,
            email = place_form.email.data,
            password = place_form.password.data)
        return redirect(url_for('home'))
    return make_response(render_template('new_place.html', place_form=place_form))

@login_required
@app.route("/home")
def home():
    resp = make_response(render_template('home.html'))
    return resp


@login_required
@app.route("/profile")
def profile():
    resp = make_response(render_template('profile.html'))
    return resp


@login_required
@app.route('/logout')
def logout():
    logout_user()
    flash("You've been logged out! Come back soon!", "success")
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
