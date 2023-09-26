import datetime
import os
import time
import cv2
import face_recognition
from moviepy.editor import VideoFileClip

def lotl_scout(known_folder,unknown_folder):
    os.system("clear")
    hits = []

    # prep work
    home = os.path.expanduser("~")

    if not os.path.exists(f"{home}/lotl_scout_output"):
        os.makedirs(f"{home}/lotl_scout_output")

    known_files = os.listdir(known_folder)
    unknown_files = os.listdir(unknown_folder)

    os.system("clear")
    print("running face recognition")

    known_image_list = []
    start = time.time()
    for _ in known_files:
        known_image = face_recognition.load_image_file(known_folder + "/" + _)
        known_image = face_recognition.face_encodings(known_image,)[0]
        known_image_list.append(known_image)
    for _ in unknown_files:
        print(f"checking {_}")
        frame_rate = VideoFileClip(unknown_folder + "/" + _).fps
        duration = int(VideoFileClip(unknown_folder + "/" + _).fps * VideoFileClip(unknown_folder + "/" + _).duration)
        capture = cv2.VideoCapture(unknown_folder + "/" + _)
        frame_position = capture.get(cv2.CAP_PROP_POS_FRAMES)
        frame_list = []
        while frame_position <= duration:
            flag,frame = capture.read()
            if flag:
                frame_position = capture.get(cv2.CAP_PROP_POS_FRAMES)
                rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                face_locations = face_recognition.face_locations(rgb_frame)
                face_encodings = face_recognition.face_encodings(rgb_frame,face_locations)
                for face_encoding in face_encodings:
                    for image in known_image_list:
                        result = bool(face_recognition.compare_faces(image,face_encodings)[0])
                        if result:
                            hits.append(f"{_} | " + str(datetime.timedelta(seconds=int(frame_position / frame_rate))))

            else:
                capture.set(cv2.CAP_PROP_POS_FRAMES,frame_position-1)

    end = time.time()
    total_time = end - start
    hits = list(set(hits[:]))
    with open(f"{home}/lotl_scout_output/matches.txt","a") as file:
        for hit in hits:
            file.write(hit + "\n")

    print("",end="\n")
    print("done in " + str(datetime.timedelta(seconds=int(total_time / frame_rate))))

os.system("clear")
known_folder = input("known folder:\n")
unknown_folder = input("unknown folder:\n")
lotl_scout(known_folder,unknown_folder)
