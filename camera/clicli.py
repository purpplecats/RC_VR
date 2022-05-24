import cv2
import numpy as np
import socket
import sys
import pickle
import struct

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.55', 8485))

cam = cv2.VideoCapture(0) #je prends la caméra par default et je lance la video

while True:
    ret,frame = cam.read()
    if ret == True:
        width = int(cam.get(3))
        height = int(cam.get(4))
    encode = cv2.VideoWriter_fourcc(*'H264')
    out = cv2.VideoWriter("filename", encode, 30, (width,height)) 
    out.write(frame)
    data = pickle.dumps(frame)
    client_socket.sendall(struct.pack("L",len(data) + data))
    
out.release()