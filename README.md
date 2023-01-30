## dadsSlideshow

#### A full sreen digital photo frame i built for my father to display his photography through a RPi and a monitor

- Once activated will display photos from the pictures folder on a continuous loop
- Requires python and OpenCV
- Transition intervals can be adjusted via line 17:

        while True:
        for photo in photos:
        img = cv2.imread(os.path.join(folder, photo))
        cv2.namedWindow("Slideshow", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Slideshow", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('Slideshow', img)
        cv2.waitKey(30000) # Display each photo for 30 seconds
