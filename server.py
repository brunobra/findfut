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
    user_form = forms.RegisterFormUser()
    place_form = forms.RegisterFormPlace()
    login_form = forms.LoginForm()
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
            password = user_form.password.data)
        return redirect(url_for('home'))
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
    return make_response(render_template('login.html', user_form=user_form, place_form=place_form, login_form=login_form))

@app.route("/home")
def home():
    resp = make_response(render_template('index.html'))
    return resp


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out! Come back soon!", "success")
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)