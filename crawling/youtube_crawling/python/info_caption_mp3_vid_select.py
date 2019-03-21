# pip install youtube_transcript_api

import os
import subprocess
import pytube
import re
from youtube_transcript_api import YouTubeTranscriptApi

url = input("input url address: ")
# https://www.youtube.com/watch?v=L3Ox-Chhjpg
# https://www.youtube.com/watch?v=ApXoWvfEYVU
yt = pytube.YouTube(url)

vids = yt.streams.all()

for i in range(len(vids)):
    print(i, '. ',vids[i])

vnum = int(input("다운 받을 화질은? "))

parent_dir = 'C:/Users/2Dub/tensorflow/crawling/youtube_video_mp3'
vids[vnum].download(parent_dir)

new_filename = input("변환 할 mp3 파일명은?")

default_filename = vids[vnum].default_filename
subprocess.call(['ffmpeg', '-i',
    os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, new_filename)
])

pat = re.compile("(v=)([a-zA-Z0-9-_]{11})")
video_id = pat.search(url).group(2)
YouTubeTranscriptApi.get_transcript(video_id)



print('Complete')
