import pytube

url = 'https://www.youtube.com/playlist?list=PLk2-liY8pARZw52zFoR8XY6wKJlEiEW6D'

playlist = pytube.Playlist(url)
for url in playlist:
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(22)
    stream.download()