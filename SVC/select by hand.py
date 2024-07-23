import cv2
import numpy as np


# Create a function based on a CV2 Event (Left button click)
ix,iy = -1,-1

# mouse callback function
def crop(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        # Then we take note of where that mouse was located
        ix,iy = x,y
           

    elif event == cv2.EVENT_LBUTTONUP:
        # crop and save image
        cv2.imwrite('by hand/img'+ num +'.jpg', img[iy:y,ix:x])

# the array that you put the number of image for crop by hand
arr = []
for i in arr:
    num = str(i).zfill(4)
    img = cv2.imread('../files/file'+ num +'.jpg')

    # This names the window so we can reference it 
    cv2.namedWindow(winname='my_drawing')
    # Connects the mouse button to our callback function
    cv2.setMouseCallback('my_drawing',crop)

    while True: #Runs forever until we break with Esc key on keyboard
        # Shows the image window
        cv2.imshow('my_drawing',img)
        
        # CHECK TO SEE IF ESC WAS PRESSED ON KEYBOARD
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # It closes all windows
    cv2.destroyAllWindows()