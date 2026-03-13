import os
import time
import pygame

## initialize pygame
pygame.mixer.init()
pygame.mixer.music.load("bad_apple.mp3")
pygame.mixer.music.play()

fps = 30
i = 0
skip = 1

## start timer for syncing
start_time = time.time()

while True:
    filename = f"frame{i}.txt"
    if not os.path.exists(filename):
        break

    ## clear terminal
    os.system("cls" if os.name == "nt" else "clear")

    ## read & print the frame
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())

    ## calculate sleep for precise syncing
    elapsed = time.time() - start_time
    sleep_time = max(0, (i / fps) - elapsed)
    time.sleep(sleep_time)
    
    i += skip

## stop music after finished
pygame.mixer.music.stop()
print("Finished playing ASCII video.")
