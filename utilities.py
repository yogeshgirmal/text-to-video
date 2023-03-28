from findimage import findimage
import os
import time

with open('text.txt', 'r') as file:
    sentence = file.read()
    words = sentence.split()
    print(words)

# Split the text into words and extract words from each sentence
data = []

for word in words:
    data.append((word))
print(data)

Img = findimage()
listf = open("list.txt", "w")
os.system('mkdir output')

count = 1
for x in data:
	Img.getImg(name=x, count=count)
	listf.write(f"file './output/{count}.mp4'\n")
	count +=1 
listf.close()
Img.close()

# Creating video for eack image (default frame rate is 2)
for x in range(1,len(data)+1):
	os.system(f'ffmpeg -framerate 2 -i ./downloads/{x}.jpg  -s 1280x720 -r 30 -pix_fmt yuv420p ./output/{x}.mp4')
	time.sleep(0.1)

time.sleep(1)
