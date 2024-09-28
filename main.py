import face_recognition
import cv2

faces=[]
names=[]

face1img=face_recognition.load_image_file("img1.jpg")
face2img=face_recognition.load_image_file("img2.jpg")
face3img=face_recognition.load_image_file("img3.jpg")

face1=face_recognition.face_encodings(face1img)[0]
face2=face_recognition.face_encodings(face2img)[0]
face3=face_recognition.face_encodings(face3img)[0]

faces.append(face1)
faces.append(face2)
faces.append(face3)

names.append("teisha")
names.append("vania")
names.append("samaira")

vc=cv2.VideoCapture(0)
while True :
    ret,frame=vc.read()
    floca=face_recognition.face_locations(frame)
    fenco=face_recognition.face_encodings(frame,floca)
    for(top,right,bottom,left), face_encoding in zip(floca, fenco):
        matches=face_recognition.compare_faces(faces, face_encoding)
        name="unknown"

        if True in matches:
            first_match_index=matches.index(True)
            name=name[first_match_index]
        
        cv2.rectangle(frame, (left,top),(right,bottom),(0,0,225),2)
        cv2.putText(frame,name,(left,top,-10),cv2.FONT_HERSHEY_COMPLEX,0.9,(0,0,225),2)

    cv2.imshow("video",frame)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

vc.release()
cv2.destroyAllWindows()
