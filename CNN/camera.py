import cv2
import pickle

filename = "finalized_40epoch_smile_detection_CNN_model.sav"
# load the face detector cascade and smile detector CNN
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
model = pickle.load(open(filename, 'rb'))

def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
        fc = frame[y:y + h, x:x + w]
        fc = cv2.resize(fc, (100, 100))
        fc = fc/255
        fc = fc.reshape((1, 100, 100, 3))
        smiling = model.predict(fc)[0]
        print(smiling)
        pred = "Smiling" if smiling > 0.1 else "Not Smiling"
        cv2.putText(frame, pred, (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

    return frame

# if a video path was not supplied, grab the reference to the webcam
def show_me():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret , frame = cap.read()
        frame = detect(frame)
        
        cv2.imshow('webcam',frame)
        if cv2.waitKey(1) & 0xFF == 0x1B:
            break
    cap.release()
    cv2.destroyAllWindows()
show_me()