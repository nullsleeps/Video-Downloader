import pytube

url = 'https://www.youtube.com/watch?v=Rl8ENE6UN2A' #change the url to the url of your choice

video = pytube.YouTube(url)

stream = video.streams.get_by_itag(22)
print("Downloading Video. . .")
stream.download(filename="Exynos") #Change the filename to the name you want
print("Finished")