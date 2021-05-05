import cv2
import time
import argparse
import numpy as np

if __name__ == '__main__':
    script_start_time = time.time()

    parser = argparse.ArgumentParser(description='Camera visualization')

    ### Positional arguments
    parser.add_argument('-i', '--cameraSource', default=0, help="Introduce number or camera path, default is 0 (default cam)")

    
    args = vars(parser.parse_args())


    cap = cv2.VideoCapture(args["cameraSource"]) #0 local o primary camera
    while cap.isOpened():
        
        success,frame = cap.read() 
        kernel = np.ones((5,5),np.float32)/25
        img = cv2.filter2D(frame,-1,kernel)    
        if not success:
            break
        if img is None:
            break

        cv2.imshow("Output", img)

        k = cv2.waitKey(10)
        if k==27:
            break


    cap.release()
    cv2.destroyAllWindows()


    print('Script took %f seconds.' % (time.time() - script_start_time))