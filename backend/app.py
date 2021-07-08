import json
import os
import logging
from flask import Flask, request, jsonify
import yaml
from .server import Server
import time
app = Flask(__name__)
server = None


@app.route("/")
@app.route("/index")
def index():
    # TODO: Add debugging information to the page if needed
    return "Much to do!"


@app.route("/init", methods=["POST"])
def initialize_server():
    # if need, client can send args(yaml format) to config server
    # args = yaml.load(request.data, Loader=yaml.SafeLoader)
    global server
    if not server:
        logging.basicConfig(
            format="%(name)s -- %(levelname)s -- %(lineno)s -- %(message)s",
            level="INFO")
        server = Server()
        os.makedirs("server_temp", exist_ok=True)
        return "New Init"


@app.route("/low", methods=["POST"])
def perform_low_images():
    result = dict(request.form)
    image = request.files["image"]
    image.save(os.path.join('../server_temp/', result['name']))
    # result = server.detect(image)
    # TODO: Detect images and save results
    return "detect success"


@app.route("/high", methods=["POST"])
def perform_high_images():
    result = json.loads(request.data)
    print(result)
    # TODO: Save results
    return "save success"
