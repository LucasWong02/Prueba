import cv2
import time
import argparse
import numpy as np

if __name__ == '__main__':
    script_start_time = time.time()

    parser = argparse.ArgumentParser(description='Camera visualization')

    ### Positional arguments
    parser.add_argument('-i', '--cameraSource', default=0,
                        help="Introduce number or camera path, default is 0 (default cam)")

    args = vars(parser.parse_args())

    cap = cv2.VideoCapture(args["cameraSource"])  # 0 local o primary camera
    while (1):
        # Take each frame
        _, frame = cap.read()
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([245, 222, 179])
        upper_blue = np.array([250, 214, 165])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()

    print('Script took %f seconds.' % (time.time() - script_start_time))


#https://docs.opencv.org/master/df/d9d/tutorial_py_colorspaces.html
