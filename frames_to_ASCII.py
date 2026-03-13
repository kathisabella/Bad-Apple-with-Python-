import cv2
import os


ascii_chars = "@%#*+=-:."

def frame_to_ascii(frame_path):
    frame = cv2.imread(frame_path, cv2.IMREAD_GRAYSCALE)
    
    ascii_str = ""

    for row in frame: 
        for pixel in row: 
            ascii_str += ascii_chars[int(pixel) * (len(ascii_chars) - 1) // 256] + " "
        ascii_str += "\n"

    return ascii_str


i = 0

while True:
    filename = f"frame{i}.jpg"

    if not os.path.exists(filename):
        break

    ascii_art = frame_to_ascii(filename)

    with open(f"frame{i}.txt", "w") as f:
        f.write(ascii_art)
    
    i += 1

print("Done converting frames.")


