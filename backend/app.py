import json
import os
import logging
import shutil

from flask import Flask, request, make_response
import yaml
from .server import Server
from utils import merge_boxes_in_results

app = Flask(__name__)


# server = Server()


@app.before_first_request
def init():
    for file in ['./low_img.txt', './high_img.txt']:
        if os.path.isfile(file):
            os.remove(file)
        f = open(file, 'w+')
        f.close()
    for dirs in ['../server_temp']:
        if os.path.isdir(dirs):
            shutil.rmtree(dirs)
        os.mkdir(dirs)


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
    result_file.write(f"{result.get('name')}, {result.getlist('shape')[0]}, {result.getlist('shape')[1]},"
                      f"{result.getlist('shape')[2]}, {result.getlist('shape')[3]}, {result.get('conf')}, {result.get('label')}\n")
    result_file.close()
    response = make_response(change_threshold)
    return response


@app.route("/high", methods=["POST"])
def perform_high_images():
    result = json.loads(request.data)
    result_file = open("high_img.txt", "a")
    result_file.write(f"{result['name']}, {result['shape'][0]}, {result['shape'][1]}, {result['shape'][2]}, {result['shape'][3]}, {result['conf']}, {result['label']}\n")
    result_file.close()
    return "save success"
