from flask import Flask, render_template, jsonify
from flask import url_for, send_from_directory
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/<string:message>/', methods=['GET', 'POST'])
def chat(message):
    return jsonify({"description": "hello "+message})
