from backend.server import Server
from utils import merge_boxes_in_results
import os

server = Server()
bandwidth = 0
image_direc = os.path.join("dataset/trafficcam_1/src/")
results_path = "trafficcam_1_gt.txt"

results_file = open(results_path, "w")
for i in range(len(os.listdir(image_direc))):
    fname = f"{str(i).zfill(10)}.png"
    image_path = image_direc + fname
    bandwidth = bandwidth + os.path.getsize(image_path)
    results, rpn_results = server.perform_detection(image_direc, 1.0, fname)
    results = merge_boxes_in_results(results.regions_dict, 0.8, 0.8)
    for region in results.regions:
        # prepare the string to write
        str_to_write = (f"{region.fid},{region.x},{region.y},"
                        f"{region.w},{region.h},"
                        f"{region.label},{region.conf}\n")
        results_file.write(str_to_write)

results_file.close()
print(f"bandwidth is {bandwidth / 1024}KB")


# bandwidth1: 518228KB
# bandwidth2: 91859KB