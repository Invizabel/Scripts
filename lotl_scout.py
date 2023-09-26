import datetime
import os
import time
import cv2
import face_recognition
from moviepy.editor import VideoFileClip

def lotl_scout(known_folder,unknown_folder):
    os.system("clear")

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
        frame_rate = VideoFileClip(unknown_folder + "/" + _).fps
        duration = int(VideoFileClip(unknown_folder + "/" + _).fps * VideoFileClip(unknown_folder + "/" + _).duration)
        capture = cv2.VideoCapture(unknown_folder + "/" + _)
        frame_position = capture.get(cv2.CAP_PROP_POS_FRAMES)
        frame_list = []
        while frame_position <= duration:
            flag,frame = capture.read()
            if flag:
                frame_position = capture.get(cv2.CAP_PROP_POS_FRAMES)
                rgb_frame = frame[:, :, ::-1]
                frame_list.append(rgb_frame)
                if len(frame_list) == 30:
                    print("#",end="",flush=True)
                    face_locations = face_recognition.batch_face_locations(frame_list,number_of_times_to_upsample=0)
                    face_encodings = face_recognition.face_encodings(frame_list,face_locations)
                    for face_encoding in face_encodings:
                        result = bool(face_recognition.compare_faces(known_image_list,face_encoding)[0])
                        if result:
                            with open(f"{home}/lotl_scout_output/matches.txt","a") as file:
                                file.write(str(datetime.timedelta(seconds=int(frame_position / frame_rate))) + "\n")

                    frame_list = []

            else:
                capture.set(cv2.CAP_PROP_POS_FRAMES,frame_position-1)

    end = time.time()
    total_time = end - start
    print("",end="\n")
    print("done in " + str(datetime.timedelta(seconds=int(total_time / frame_rate))))

os.system("clear")
known_folder = input("known folder:\n")
unknown_folder = input("unknown folder:\n")
lotl_scout(known_folder,unknown_folder)
