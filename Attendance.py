import cv2 as c
import numpy as np
import face_recognition as fc
import os
from datetime import datetime as dt

path = 'basic images'
images = []
classes = []
mylist = os.listdir(path)

#print(mylist)

for item in mylist:
    currentImage = c.imread(f'{path}\{item}')
    images.append(currentImage)
    classes.append(os.path.splitext(item)[0])
# print(classes)
# print(images)

def findEncodings(image):
    encodeList = []
    for img in image:
        img = c.cvtColor(img, c.COLOR_BGR2RGB)
        encode = fc.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('AttendanceRec.csv', 'r+') as f:
        myDataList = f.readlines()
        # print(myDataList)

        nameList = []
        # nameList.clear()

        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = dt.now()
            dtString = now.strftime('%H:%S:%M')
            f.writelines(f'\n{name},{dtString}')




encodedList = findEncodings(images)
#print(len(encodedList))
# print(encodedList)

cap = c.VideoCapture(0)

while True:
    ret, frame = cap.read()
    img = c.resize(frame, (800, 600))
    #img = c.resize(frame, (0,0), None, 0.25, 0.25)          #one fourth of the size...0.25
    gray = c.cvtColor(img, c.COLOR_BGR2RGB)

    faceLocations = fc.face_locations(gray)
    encodedFrame = fc.face_encodings(gray, faceLocations)

    for faceLoc, encode in zip(faceLocations, encodedFrame):
        mathches = fc.compare_faces(encodedList, encode)
        faceDis = fc.face_distance(encodedList, encode)
        # print(faceDis)

        matchIndex = np.argmin(faceDis)            #with minumum face distance

        if mathches[matchIndex]:
            name = classes[matchIndex].upper()
            print(name)

            y1, x2, y2, x1 = faceLoc
            #y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            c.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            c.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), c.FILLED)
            c.putText(img, name, (x1+6, y2-12), c.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)

            markAttendance(name)

    c.imshow('Image', img)
    c.waitKey(1)
