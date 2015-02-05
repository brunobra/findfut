from flask import Flask, request, make_response, render_template


app = Flask(__name__)


@app.route("/")
def index():
    resp = make_response(render_template('login.html'))
    return resp

@app.route("/login", methods=['POST'])
def login():
    content = request
    print content
    return "OK"

@app.route("/sigin", methods=['POST'])
def sigin():
    content = request.json
    print content
    return "OK"


if __name__ == "__main__":
    app.debug = True
    app.run()