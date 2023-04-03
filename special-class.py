import cv2
import vlc
import numpy as np


class Special():

    
    def __init__(self, work) :
        detectFace = cv2.CascadeClassifire("lib/haarcascade_frontalface_default.xml")
        detectEye = cv2.CascadeClassifire("lib/haarcascade_eye.xml")

        if work == "eye":
            self.camera()
        else:
            self.media(work)

    
    def camera(self):
        pass
    def media(self,work):
        pass
