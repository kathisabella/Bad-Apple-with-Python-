## extract the frames from the file 'bad_apple.mp4' using OpenCV-Python
import cv2

vid = cv2.VideoCapture("bad_apple.mp4") ## creates a capture object

count = 0
success = True

## resize the frames, easier to be processed by the terminal
width = 54
height = 40


while success:
    success, frame = vid.read() ## reads the next frame, returns boolean and the frame
    if success:
        resized_frame = cv2.resize(frame, (width, height)) ## frame resizing
        grayscale = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imwrite(f"frame{count}.jpg", grayscale) ## save individual frame (already RESIZED & GRAYSCALE)
        count += 1

vid.release()

## this should output 6955 frames 

