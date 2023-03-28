import os
import time

os.system('ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4')
time.sleep(1)
os.system('ffmpeg -i output.mp4 -i text.mp3 -c:v copy -c:a aac text_to_video.mp4')
time.sleep(1)
print('text_to_video has created')