from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

if __name__ == "__main__":
    Download('https://www.youtube.com/watch?v=t4rMkxTQc04&t=352s')