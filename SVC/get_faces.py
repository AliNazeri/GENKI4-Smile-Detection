import cv2

# Load the cascade
arr = []
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
for i in range(1,4001):
    num = str(i).zfill(4)
    img = cv2.imread('../files/file'+ num +'.jpg')
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.2, 6)
    
    # check if it is inly one face
    if len(faces) != 1:
        j = 1
        # look for a setting to obtain a single face
        while(len(faces) != 1):
            faces = face_cascade.detectMultiScale(gray, 1.1, j)
            j+=1
            if(len(faces) == 0):
                break

        # check again if the is found
        # if it is not save the number of image then go for next one
        # if it detect one face, the image will be croped and saved
        if len(faces) != 1:
            arr.append(i)
            continue
        else:
            (x, y, w, h) = faces[0]
            res = img[y:y+h,x: x+w]
            cv2.imwrite('newimg/img'+ num +'.jpg', res)
    else:
        (x, y, w, h) = faces[0]
        res = img[y:y+h,x: x+w]
        cv2.imwrite('newimg/img'+ num +'.jpg', res)

# check in how many images couldnt find any face
print(arr,len(arr))
