from backend.server import Server
from utils import merge_boxes_in_results
import os

server = Server()
image_direc = os.path.join("server_temp")
fname = f"{str(15).zfill(10)}.png"

results, rpn_results = server.perform_detection(image_direc, 1.0, fname)
results = merge_boxes_in_results(results.regions_dict, 0.3, 0.3)
results.write("test.txt")
