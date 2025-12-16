import cv2
import os

def video_to_image(filename):
    print(f"converting: {filename} to audio")
    os.system(f"ffmpeg -i {filename} output.wav")
    print(f"converting: {filename} to images")
    cap = cv2.VideoCapture(filename)
    frame_idx = 0

    if not os.path.exists("IN"):
        os.makedirs("IN")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_filename = f"IN/{os.path.splitext(filename)[0]}_frame_{frame_idx:010d}.png"
        cv2.imwrite(frame_filename, frame)
        frame_idx += 1

    cap.release()
    print(f"Extracted {frame_idx} frames from {filename}")

def image_to_video(filename,framerate):
    os.system(f"ffmpeg -framerate {framerate} -i OUT/{filename}_frame_%010d.png  old_output.mkv")
    os.system(f"ffmpeg -i output.mkv -i output.wav  output.mkv")
    os.remove("old_output.mkv")

mode = input("1 = Video2Frames | 2 = Frames2Video\n")
if mode == "1":
    filename = input("filename: ")
    video_to_image(filename)

if mode == "2":
    filename = input("filename: ")
    framerate = input("frame rate: ")
    image_to_video(filename,framerate)
