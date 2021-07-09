import cv2
import glob
import os
import re
from datetime import datetime


# Video path
VIDEO = "./test.mp4"
# Frames path
FRAMES = "./extracted_frames"


def video_to_frames():
    video_capture = cv2.VideoCapture()
    video_capture.open(VIDEO)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    frames = video_capture.get(cv2.CAP_PROP_FRAME_COUNT)
    print("fps=", int(fps), "frames=", int(frames))
    if not os.path.exists(FRAMES):
        os.makedirs(FRAMES)
    for i in range(int(frames)):
        ret, frame = video_capture.read()
        frame_name = f"{str(i).zfill(10)}.png"
        cv2.imwrite("./extracted_frames/" + frame_name, frame)


if __name__ == '__main__':
    video_to_frames()
