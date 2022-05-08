from flask import render_template, redirect, url_for, request, jsonify
from base64 import b64encode, b64decode
from server import app
import requests

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/proxy/<string:path>", methods=["GET"])
def proxy(path):
    page = requests.get(b64decode(path.encode()).decode()).content
    return page

@app.route("/api", methods=["POST"])
def api():
    print("YES")
    return redirect("/proxy/" + b64encode(request.form["url-input"].encode()).decode())
