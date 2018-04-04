"""
Example of serving a data model object as json via flask

To run, cd to directory:
FLASK_APP=flask_serve_json.py flask run
"""

import json
from flask import Flask, redirect, url_for


app = Flask(__name__)
ROUTE_GETJSON = '/getjson'


@app.route('/')
def index():
    return redirect(url_for('serveJson'))


@app.route('/getjson')
def serveJson():
    keyworded_params = {
        "param1": "test data",
        "param2": "testing",
        "param3": ["some", "more", "data"]
    }
    data_model = MockDataModel(**keyworded_params)

    return json.dumps(data_model.__dict__)


class MockDataModel:
    def __init__(self, param1, param2, param3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

