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
    print("6 --> Escala de grises")
    print("7 --> Efecto acuarela")
    
    filtro = int(input("Elija el filtro de su preferencia: ", ))

    script_start_time = time.time()

    parser = argparse.ArgumentParser(description='Camera visualization')

    ### Positional arguments
    parser.add_argument('-i', '--cameraSource', default=0, help="Introduce number or camera path, default is 0 (default cam)")

    
    args = vars(parser.parse_args())


    cap = cv2.VideoCapture(args["cameraSource"]) #0 local o primary camera
    
    
    while cap.isOpened():
        
        if filtro == 1:
            a = "camara sin efecto"
            success,img = cap.read()    
            
            if not success:
                break
            if img is None:
                break
            
        elif filtro ==2:
            a = "inversion de colores"
            ret, frame = cap.read()
            img = cv2.bitwise_not(frame)
            if not ret:
                break
            if img is None:
                break
            
        elif filtro ==3:
            a = "difuminado"
            success,frame = cap.read() 
            kernel = np.ones((5,5),np.float32)/25
            img = cv2.filter2D(frame,-1,kernel)
        
        elif filtro ==4:
            a = "de cabeza"
            success,img = cap.read()    
            img = cv2.flip(img,0)
            if not success:
                break
            if img is None:
                break
            
        elif filtro == 5:
            a = "resaltar color"
            _, frame = cap.read()
            # Convert BGR to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # define range of blue color in HSV
            lower_blue = np.array([245, 222, 179])
            upper_blue = np.array([250, 214, 165])
            # Threshold the HSV image to get only blue colors
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            # Bitwise-AND mask and original image
            img = cv2.bitwise_and(frame, frame, mask=mask)
            
        elif filtro ==6:
            a = "escala de grises"
            success,img = cap.read()    
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            if not success:
                break
            if img is None:
                break
            
        elif filtro ==7:
            a = "acuarela"
            success,img = cap.read() 
            img = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
            if not success:
                break
            if img is None:
                break
        
        else:
            print("Error en la selección")
        
        flip = cv2.flip(img,1)
        cv2.imshow(a,flip)
        k = cv2.waitKey(10)
        if k==27:
            break

    cap.release()
    cv2.destroyAllWindows()


    print('Script took %f seconds.' % (time.time() - script_start_time))
