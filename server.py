from flask import Flask, request, make_response, render_template, redirect, flash, url_for
from flask.ext.login import LoginManager

import forms
import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'


app = Flask(__name__)
app.secret_key = 'futeba_app'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
  try:
    return models.User.get(models.User.id == userid)
  except models.DoesNotExist:
    return None


@app.route("/", methods=['GET', 'POST'])
def index():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash("Registered!", "success")
        models.User.create_user(
            username = form.username.data,
            bday = form.bday.data,
            genre = form.genre.data,
            address = form.address.data,
            city = form.city.data,
            state = form.state.data,
            email = form.email.data,
            password = form.password.data
            )
        return redirect(url_for('home'))
    return make_response(render_template('login.html', form=form))

@app.route("/home")
def home():
    resp = make_response(render_template('index.html'))
    return resp


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)