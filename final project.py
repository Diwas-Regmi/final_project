#!/usr/bin/env python
# coding: utf-8

# In[1]:


# # installing dlib
get_ipython().system('pip install dlib')


# In[2]:


# installing face recognition
get_ipython().system('pip install face_recognition')


# In[3]:


# installing opencv
get_ipython().system('pip install opencv-python')


# In[4]:


import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import pickle


# In[5]:


path = r'C:\Users\Acer\OneDrive\Desktop\Students'


# In[6]:


images = []
classNames = []

mylist = os.listdir(path)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])


# In[7]:


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    return encodeList
encoded_face_train = findEncodings(images)


# In[8]:


def markAttendance(name):
    with open(r"C:\Users\Acer\OneDrive\Desktop\attendance.csv",'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'n{name}, {time}, {date}')


# In[ ]:


# Initialize webcam
cap = cv2.VideoCapture(0)

# Define a function to mark attendance (placeholder)
def markAttendance(name):
    print(f"Attendance marked for {name}")

# Assume `encoded_face_train` and `classNames` are defined earlier in your code
# Example: encoded_face_train = [array_of_encodings]
# Example: classNames = ["Name1", "Name2", ...]

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture frame")
        break

    # Resize and convert to RGB
    imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Find faces in frame
    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

    for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
        # Compare faces
        matches = face_recognition.compare_faces(encoded_face_train, encode_face)
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face)

        matchIndex = np.argmin(faceDist)
        if matches[matchIndex]:
            name = classNames[matchIndex].lower()
            y1, x2, y2, x1 = faceloc

            # Scale back to the original image size
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            # Draw rectangle and text
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            # Mark attendance
            markAttendance(name)

    # Display the webcam feed
    cv2.imshow('Webcam', img)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:






