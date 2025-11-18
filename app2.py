import os
import flask
from flask import request

app = flask.Flask(__name__)

# Hardcoded credentials (security issue)
USERNAME = "admin"
PASSWORD = "password123"

@app.route("/eval", methods=["GET"])
def insecure_eval():
    code = request.args.get("code")
    return str(eval(code))  #  Arbitrary code execution

@app.route("/cmd", methods=["POST"])
def insecure_command():
    cmd = request.form.get("cmd")
    os.system(cmd)  #  Command injection
    return "Command executed"

@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("username")
    pw = request.form.get("password")
    if user == USERNAME and pw == PASSWORD:
        return "Welcome admin"
    return "Unauthorized"

if __name__ == "__main__":
    app.run(debug=True)
