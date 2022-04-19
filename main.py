from pytube import Playlist
import pathlib

print("Welcome to youtube playlist downloader !")

link = input("Please paste the playlist link: ")
directory = pathlib.Path(input("Please paste where to save the videos: "))
playlist = Playlist(link)
total = len(playlist.videos)
try :
    i = 0
    for video in playlist.videos:
        print(f"Downloading........ {video.title}")
        video.streams.get_highest_resolution().download(directory)
        i += 1
        print(f"{i}/{total} video(s) downloaded !")

    print(f"Thankyou for using this downloader. All videos are downloaded and saved at {directory}")
except:
    print("Some error occurred. Please try again !")


