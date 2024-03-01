import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import dlib
import cv2
import face_recognition
from Aspira.interview import Interview
import time
import datetime
from Aspira.bot import BOT

os.makedirs("extracted_faces", exist_ok=True)

# Add the parent directory to the Python path

# Now you should be able to import modules from the sibling directory
from Intellexi.conn.mongodb import get_upcoming_interviews

from Intellexi.conn.mongodb import get_upcoming_interviews


class KYC:
    def __init__(self, id, interview_time, image_path) -> None:
        self.id = id
        self.interview_time = interview_time
        self.image_path = image_path
        self.face_cascade=cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        self.detector=dlib.get_frontal_face_detector()
        self.all_detected_faces=[]

    def extractfaces(self,path=None):
        os.makedirs(f"extracted_faces/{self.id}", exist_ok=True)
        if path:
            image = cv2.imread(path)
        else:
            image=cv2.imread(self.image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = self.face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        # Extract faces and save them
        for i, (x, y, w, h) in enumerate(faces):
            face = image[y : y + h, x : x + w]
            cv2.imwrite(f"extracted_faces/{self.id}/{i}.jpg", face)
            print(f"Face {i+1} extracted and saved successfully!")
            path=f"extracted_faces/{self.id}/{i}.jpg"
            self.all_detected_faces.append(path)
        return self.all_detected_faces
    
    def match_face(self,meeting_screenshot_path):
        matches=False
        each=self.all_detected_faces[0]
        print(each)
        reference_image = face_recognition.load_image_file(each)
        try:
            reference_encoding = face_recognition.face_encodings(reference_image)[0]
        except :
            pass
        image = cv2.imread(meeting_screenshot_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = self.detector(gray)
        print(faces)
        print("----------------")
        for face in faces:
            print(face)
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            face_image = image[y : y + h, x : x + w]
            face_image_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
            face_encoding = face_recognition.face_encodings(face_image_rgb)
            cv2.imwrite("face_image_{face}.jpg", face_image)
            if len(face_encoding) > 0:
                match = face_recognition.compare_faces(
                    [reference_encoding], face_encoding[0]
                )
                if match[0]:
                    print("Match found! This is the reference face.")
                    cv2.imshow("matched", face_image)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    # return True
                    matches=True
                else:
                    print("No match found.")
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print("-------------matched atleat once ------------",matches)
        return matches

    def start_interview(self):
        interview=Interview(questions_excel_sheet_path="path")
        interview.start_interview()


while True:
    print("True")
    interviews = get_upcoming_interviews()

    print("interview_data:  ", interviews)

    if not interviews:
        print("No interview data available")
        print("Interview data is empty. WIll fetch again in a minute...")
        time.sleep(10)
        continue

    for item in interviews:
        name = item.get("name", "No Name")
        meetingTime = item.get("meetingtime", None)
        meeting_link = item.get("meetingurl", "No Meeting Link")
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M")
        datetime_obj = datetime.datetime.strptime(meetingTime, "%Y-%m-%dT%H:%M")
        formatted_meettime_str = datetime_obj.strftime("%Y-%m-%d %H:%M")

        print(current_time, formatted_meettime_str)
        if current_time == formatted_meettime_str:
            print("yes")
            BOT(meet_url=meeting_link, name=name)
        else:
            print("not the time")
        print(
            "next--------------------------------------------------------------------------------"
        )

    schedule.run_pending()

# kyc = KYC(
#     id="65ddcb219a86fc210c7a4189",
#     interview_time="",
#     image_path="ss3.png",
# )

# kyc.extractfaces()
# extarcted_face_image=kyc.extractfaces(path="ss3.png")
# for each in extarcted_face_image:
#     kyc.match_face(meeting_screenshot_path=each)

# print("matched")
