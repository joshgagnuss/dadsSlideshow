import cv2
import os
import time

# Specify the folder containing the photos
folder = 'pictures'

# Get a list of all the photos in the folder
photos = [photo for photo in os.listdir(folder) if photo.endswith('.jpg')]

# Loop through each photo and display it
for photo in photos:
    img = cv2.imread(os.path.join(folder, photo))
    cv2.imshow('Slideshow', img)
    cv2.waitKey(20000)  # Display each photo for 3 seconds