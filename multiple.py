import pytube

video_list = []

print("Enter Url")
while True:
    url = input("")
    if url == "Start": #Type Start then press enter to start the downloading 
        break
    video_list.append(url)

for x, video in enumerate(video_list):
    v = pytube.YouTube(video)
    stream = v.streams.get_by_itag(22)
    print(f"Downloading video {x}...")
    stream.download()
    print("finished!")