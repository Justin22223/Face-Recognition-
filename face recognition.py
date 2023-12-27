import cv2
from deepface import DeepFace

def face_recognition(frame):
    result = DeepFace.verify(frame, reference_img)
    return result["verified"]

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 470)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 650)

counter = 0
reference_img = cv2.imread("mom.jpg")

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            face_match = face_recognition(frame)

        if face_match:
            cv2.putText(frame, "Face Match", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, "No Match", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow("Face Recognition", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()