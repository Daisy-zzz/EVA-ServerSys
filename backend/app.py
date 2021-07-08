import json
import os
import logging
from flask import Flask, request
import yaml
from .server import Server
from utils import merge_boxes_in_results
app = Flask(__name__)
# server = Server()

resolution = 1


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
    # temp = []
    # results, rpn_results = server.perform_detection('../server_temp/', resolution, result['name'])
    # results = merge_boxes_in_results(results.regions_dict, 0.3, 0.3)
    # for region in results.regions:
    #     temp.append([region.x, region.y, region.w, region.h, region.conf])
    print(result['name'])
    return "detect success"


@app.route("/high", methods=["POST"])
def perform_high_images():
    result = json.loads(request.data)
    print(result)
    # TODO: Save results
    return "save success"
