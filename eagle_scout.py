import io
import multiprocessing
import os
import time
import face_recognition
from moviepy.editor import VideoFileClip
from PIL import Image

def convert_files(_,unknown_folder):
    home = os.path.expanduser("~")
    video = VideoFileClip(unknown_folder + "/" + _)
    video.write_gif(f"{home}/unbound_now/{_}.gif",program="ffmpeg")

def process_images(_,__,known_folder,unknown_folder):
    home = os.path.expanduser("~")
    if __.endswith(".gif"):
        try:
            image = Image.open(home + "/unbound_now/" + __)
            for ___ in range(image.n_frames):
                try:
                    image.seek(___)
                    buffer = io.BytesIO()
                    image.save(buffer,format="png")
                    known_file = face_recognition.load_image_file(known_folder + "/" + _)
                    unknown_file = face_recognition.load_image_file(buffer)
                    known_file = face_recognition.face_encodings(known_file)[0]
                    unknown_file = face_recognition.face_encodings(unknown_file)[0]
                    result = bool(face_recognition.compare_faces([known_file],unknown_file)[0])
                    if result:
                        image.save(f"{home}/unbound_now_output/{_} == {__} | frame: {___}.png",format="png")
                        with open("matches.txt","a") as file:
                            file.write(f"{_} == {__} | frame: {___}\n")

                except IndexError:
                    continue

        except:
            print(f"ERROR: {__}")

def eagle(known_folder,unknown_folder):
    os.system("clear")

    # prep work
    home = os.path.expanduser("~")
    if not os.path.exists(f"{home}/unbound_now"):
        os.makedirs(f"{home}/unbound_now")

    if not os.path.exists(f"{home}/unbound_now_output"):
        os.makedirs(f"{home}/unbound_now_output")

    core_count = multiprocessing.cpu_count()
    

    known_files = os.listdir(known_folder)
    unknown_files = os.listdir(unknown_folder)

    p_list = []
    core_tracker = 0
    for _ in unknown_files:
        core_tracker += 1
        p = multiprocessing.Process(target=convert_files,args=(_,unknown_folder))
        p_list.append(p)
        p.start()
        if core_tracker % core_count == 0:
            for __ in p_list:
                __.join()

    for __ in p_list:
        __.join()

    os.system("clear")
    print("running facial recognition")
    unknown_files = os.listdir(f"{home}/unbound_now")

    p_list = []
    core_tracker = 0
    start = time.time()
    for _ in known_files:
        for __ in unknown_files:
            core_tracker += 1
            p = multiprocessing.Process(target=process_images,args=(_,__,known_folder,unknown_folder))
            p_list.append(p)
            p.start()
            if core_tracker % core_count == 0:
                for __ in p_list:
                    __.join()

    for __ in p_list:
        __.join()

    end = time.time()
    print("done in " + str(end - start) + " seconds")

known_folder = input("known folder:\n")
unknown_folder = input("unknown folder:\n")
eagle(known_folder,unknown_folder)
