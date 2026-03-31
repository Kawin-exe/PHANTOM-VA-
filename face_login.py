import cv2
import face_recognition

def login():
    cam = cv2.VideoCapture(0)

    known_image = face_recognition.load_image_file("user.jpg")
    known_encoding = face_recognition.face_encodings(known_image)[0]

    print("Scanning face...")

    while True:
        ret, frame = cam.read()
        rgb = frame[:, :, ::-1]

        faces = face_recognition.face_encodings(rgb)

        for face in faces:
            match = face_recognition.compare_faces([known_encoding], face)
            if True in match:
                print("Access Granted")
                cam.release()
                return True

        cv2.imshow("Login", frame)
        if cv2.waitKey(1) == 27:
            break

    cam.release()
    return False
