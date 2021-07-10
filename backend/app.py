import json
import os
import logging
from flask import Flask, request, make_response
import yaml
from .server import Server
from utils import merge_boxes_in_results
app = Flask(__name__)
# server = Server()


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
    change_threshold = "0.0"
    result = request.form
    image = request.files["image"]
    image.save(os.path.join('../server_temp/', result['name']))
    result_file = open("low_img.txt", "a")
    result_file.write(f"{result.get('name')}, {result.getlist('shape')}, {result.get('conf')}\n")
    result_file.close()
    response = make_response(change_threshold)
    return response


@app.route("/high", methods=["POST"])
def perform_high_images():
    result = json.loads(request.data)
    result_file = open("high_img.txt", "a")
    result_file.write(f"{result['name']}, {result['shape']}, {result['conf']}\n")
    result_file.close()
    return "save success"
