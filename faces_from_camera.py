# This is a demo of running face recognition on a Raspberry Pi.
# This program will print out the names of anyone it recognizes to the console.

# To run this, you need a Raspberry Pi 2 (or greater) with face_recognition and
# the picamera[array] module installed.
# You can follow this installation instructions to get your RPi set up:
# https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65

import face_recognition
import cv2
import numpy as np


cap = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []
face_encodings = []

while True:
#    print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    ret, frame = cap.read()

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(frame)
#    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(frame, face_locations)
#    print(face_locations )
    for face in face_locations:
        cv2.rectangle(frame, (face[1],face[0]), (face[3],face[2]), (0,255,0),3)
    cv2.imshow('frame',frame)

    # Loop over each face found in the frame to see if it's someone we know.
#    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
#        match = face_recognition.compare_faces([obama_face_encoding], face_encoding)
#        name = "<Unknown Person>"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#        if match[0]:
#            name = "Barack Obama"

#print("I see someone named {}!".format(name))
cap.release()
cv2.destroyAllWindows()
