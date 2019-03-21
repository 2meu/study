import requests
import json

movie_trailer_info = {
    'title': '',
    'publishedAt': '',
    'description': '',
    'defaultLanguage': ''
}

def get_trailer_video_link(target_url):
    reponse = requests.get(target_url).text
    items = json.loads(response)
    title = items['items'][0]['snippet']['title']
    publishedAt = items['items'][0]['snippet']['publishedAt']
    description = items['items'][0]['snippet']['description']
    defaultLanguage = items['items'][0]['snippet']['defaultLanguage']
    movie_trailer_info = {
    'title': title,
    'publishedAt': publishedAt,
    'description': description,
    'defaultLanguage': defaultLanguage
    }
    return movie_trailer_info

apiKey ='AIzaSyBt3aTnFJz9zvryJq-tHe3wq7hNzjJtjK0'
target_url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id=JyGGLB542ks&' + '&key=' + apiKey

get_trailer_video_link(target_url)

# print(items['items'][0]['snippet']['publishedAt'])
# print(items['items'][0]['snippet']['title'])
# print(items['items'][0]['snippet']['description'])
