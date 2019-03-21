from pytube import YouTube

url = input("Put Youtube video link: ")
#https://www.youtube.com/watch?v=2zR1GOLhlU4&t=1s
#https://www.youtube.com/watch?v=IKae08TUnCE&t=6s
#https://www.youtube.com/watch?v=wVYFVjSFXGA

yt = YouTube(url)
stream = yt.streams.first()
stream.download('C:/Users/2Dub/tensorflow/crawling/youtube_video')
