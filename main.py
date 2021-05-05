import cv2
import time
import argparse
import numpy as np

if __name__ == '__main__':
    print("1 --> Sin filtro")
    print("2 --> Inversión de colores")
    print("3 --> Difuminado de imagen")
    print("4 --> De cabeza")
    print("5 --> Resaltado de azul")
    filtro = int(input("Elija el filtro de su preferencia: ", ))

    script_start_time = time.time()

    parser = argparse.ArgumentParser(description='Camera visualization')

    ### Positional arguments
    parser.add_argument('-i', '--cameraSource', default=0, help="Introduce number or camera path, default is 0 (default cam)")

    
    args = vars(parser.parse_args())


    cap = cv2.VideoCapture(args["cameraSource"]) #0 local o primary camera
    
    
    while cap.isOpened():
        
        if filtro == 1:
            #BGR image feed from camera
            success,img = cap.read()    
            
            if not success:
                break
            if img is None:
                break
            
        elif filtro ==2:
            ret, frame = cap.read()
            img = cv2.bitwise_not(frame)
            if not ret:
                break
            if img is None:
                break
            
        elif filtro ==3:
            success,frame = cap.read() 
            kernel = np.ones((5,5),np.float32)/25
            img = cv2.filter2D(frame,-1,kernel)
        
        elif filtro ==4:
            success,img = cap.read()    
            img = cv2.flip(img,0)
            if not success:
                break
            if img is None:
                break
        #
        flip = cv2.flip(img,1)
        cv2.imshow("Camera",flip)
        k = cv2.waitKey(10)
        if k==27:
            break

    cap.release()
    cv2.destroyAllWindows()


    print('Script took %f seconds.' % (time.time() - script_start_time))


