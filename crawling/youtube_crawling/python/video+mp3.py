import os
import subprocess
import pytube

url = input("input url address: ")
# https://www.youtube.com/watch?v=L3Ox-Chhjpg
# https://www.youtube.com/watch?v=ApXoWvfEYVU
yt = pytube.YouTube(url)

vids = yt.streams.all()

for i in range(len(vids)):
    print(i, '. ',vids[i])

vnum = int(input("다운 받을 화질은? "))

parent_dir = 'C:/Users/2Dub/youtube_video_mp3'
vids[vnum].download(parent_dir)

new_filename = input("변환 할 mp3 파일명은?")

default_filename = vids[vnum].default_filename
# vids[vnum] = <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2">
# vids[vnum].default_filename = Captive State Teaser Trailer 1 (2019)  Movieclips Trailers.mp4

subprocess.call(['ffmpeg', '-i',
    os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, new_filename)
])

print('Complete')
