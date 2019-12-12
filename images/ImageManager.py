import tkinter as tk
import os.path


def grab_frames(photo_name, total_frames):
    frames = []
    count = 0
    while count < total_frames:
        parts = photo_name.split(".")
        parts[0] = parts[0]+str(count)
        temp_name = parts[0]+"."+parts[1]
        frames.append(tk.PhotoImage(file=os.path.join('images\\'+photo_name.split(".")[0], temp_name)))
        count += 1
    return frames
