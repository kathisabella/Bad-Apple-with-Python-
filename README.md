# Bad-Apple-with-Python-
This project recreates the “Anything can be Bad Apple!!” meme using Python in the terminal. It plays the music video using ASCII art synchronized with the original music.

The [Bad Apple!! music video](https://www.youtube.com/watch?v=i41KoE0iMYU&list=RDi41KoE0iMYU&start_radio=1) is taken from the YouTube Channel [Alstroemeria Records](https://www.youtube.com/@AlstroemeriaRecords).

## Prerequisites:

We are using the the **OpenCV-Python** library to extract the frames from the `bad_apple.mp4` file. If you don't have it already, it can be installed using:
```bash
pip install opencv-python
```

All the required video `bad_apple.mp4` and audio `bad_apple.mp3` files are already provided so you don't have to find and download them.

## Files Provided in the Repository:
Inside this repository will be 3 python `.py` files: 

1. `extract_frames.py` – extracts frames from the video (.jpg)
2. `frames_to_ASCII.py` – converts each frame to ASCII (.txt)
3. `play_ASCII.py` – plays the ASCII video with music in the terminal

## How to Run:

These 3 python files need to be run in this exact order. 

1. Run the **extract_frames.py** file to extract the frames from the `bad_apple.mp4` video. If done correctly, this should extract **6955** numbered `.jpg` frames (zero-inclusive). 

```
python3 extract_frames.py
```

2. Run the **frames_to_ASCII.py** file to convert each individual frames into ASCII art. Again, if done correctly, this should create **6955** numbered `.txt` files  (zero-inclusive). 

```
python3 frames_to_ASCII.py
```

3. Run the **play_ASCII.py** file and enjoy!

```
python3 play_ASCII.py
```
Just run the scripts consecutively — you don’t need to do anything while they are running.
