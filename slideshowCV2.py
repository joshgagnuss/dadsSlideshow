import cv2
import os
import time

# Specify the folder containing the photos
folder = 'pictures'

# Get a list of all the photos in the folder
photos = [photo for photo in os.listdir(folder) if photo.endswith('.jpg')]

while True:
    for photo in photos:
        img = cv2.imread(os.path.join(folder, photo))
        cv2.namedWindow("Slideshow", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Slideshow", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('Slideshow', img)
        cv2.waitKey(30000)  # Display each photo for 30 seconds
