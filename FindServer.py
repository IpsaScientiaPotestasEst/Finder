from flask import Flask, jsonify, request
from flask_cors import CORS
import json


app = Flask(__name__)

CORS(app)

last_location = {"lat": None, "lon": None}

@app.route("/msg",methods=["POST"])
def msg():
    global last_location
    data = json.loads(request.data)
    last_location["lat"] = data["lat"]
    last_location["lon"] = data["lon"]
    return jsonify({"status":"saved"})

@app.route("/get_location",methods=["GET"])
def get_location():
    return jsonify(last_location)
    

