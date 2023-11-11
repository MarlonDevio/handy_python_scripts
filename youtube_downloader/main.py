from sys import argv
from pytube import YouTube

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
