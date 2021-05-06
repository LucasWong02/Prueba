import cv2
import time
import argparse

import glob
import math
import os

if __name__ == '__main__':
    script_start_time = time.time()

    parser = argparse.ArgumentParser(description='Camera visualization')

    ### Positional arguments
    parser.add_argument('-i', '--cameraSource', default=0, help="Introduce number or camera path, default is 0 (default cam)")

    
    args = vars(parser.parse_args())


    cap = cv2.VideoCapture(args["cameraSource"]) #0 local o primary camera
    
        
    def apply_invert(frame):
        return cv2.bitwise_not(frame)
    
    while (True):
        ret, frame = cap.read()
        invert = apply_invert(frame)
        cv2.imshow('invert',invert)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break                

    cap.release()
    cv2.destroyAllWindows()


    print('Script took %f seconds.' % (time.time() - script_start_time))