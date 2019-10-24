#python3 script to download vedios from youtube

from __future__ import unicode_literals
import youtube_dl
import os

ydl_opts = {}
print("==================== path check ========================")

#path where vedio will store after download
path = '/home/username/Videos'


os.chdir(path)
print("vedio URl:")

#input vedio URL on youtube
link = input()
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
