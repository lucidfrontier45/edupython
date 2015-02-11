from flask import Flask, request
import traceback

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


try:
    from .app1 import app1 as _app1

    app1_ok = True
except:
    app1_err = traceback.format_exc()
    app1_ok = False


@app.route("/api/app1", methods=["POST"])
def app1():
    if not app1_ok:
        return app1_err, 500

    try:
        x = request.form.get("x")
        y = request.form.get("y")
        return str(_app1(int(x), int(y)))
    except Exception as e:
        return str(traceback.format_exc()), 500

@app.route("/index1")
def index1():
    return app.send_static_file("index1.html")