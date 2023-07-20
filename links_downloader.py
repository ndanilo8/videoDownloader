# Author: Danilo Nascimento
# E-mail: me@daniloinspace.com


from yt_dlp import YoutubeDL
import sys

# Script to download multiple videos or music from a .txt file containing their respective links

# Pre-Requisites:
# yt-dlp
# ffmpeg

# Usage Steps:
# 1. python links_downlaoder.py (mp3/mp4) <links.txt>
# 2. Enjoy the downloaded files at same location as the .py


try:
    Type = sys.argv[1]
    links_txt = sys.argv[2]
    file = open(links_txt, "r")
except:
    print("Error missing arguments!")
    print("python links_downloader.py (mp3/mp4) <links.txt>")
    sys.exit(0)

if Type.lower() == "mp3":
    # yt-dlp API Call
    ydl_opts = {
        'format': 'bestaudio/best',
        "writethumbnail": True,
        "outtmpl": "%(title)s.%(ext)s",
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            },
            {
                "key": "FFmpegMetadata",
            },
            {
                "key": "EmbedThumbnail",
            },
        ],
    }

    print("\n       Download Completed...Enjoy!")
elif Type.lower() == "mp4":
    # yt-dlp API Call
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        "writethumbnail": True,
        "outtmpl": "%(title)s.%(ext)s",
        'postprocessors': [
            {
                "key": "FFmpegMetadata",
            },
            {
                "key": "EmbedThumbnail",
            },
        ],
    }

with YoutubeDL(ydl_opts) as ydl:
        for link in file:
            ydl.download(link)

print("\n\nDownload Completed...Enjoy!")
