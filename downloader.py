# Author: Danilo Nascimento
# E-mail: danilo@daniloonspace.com



from yt_dlp import YoutubeDL

# Script to download to videos/music from a .txt file

# Pre-Requisites:
# yt-dlp
# ffmpeg

# Usage Steps:
# 1 Step: Add urls to a "links.txt" file same location as this script
# 2 Step: Run script and choose 1 or 2 for video or audio download.
# 3 Step: Enjoy!


def main():
    # Check links.txt file
    try:
        file = open("links.txt", "r")
    except OSError:
        print("Could not open/read file:", fname)
        sys.exit()

    # Check the file format requested

    try:
        file_format = input(
            "Select the file format:\n Type 1 for video&audio\n Type 2 for audio-only\n")
    except ValueError:
        print("That was no valid number...")

    # yt-dlp API Call
    if(file_format == '1'):
        ydl_opts = {
            'format': 'best',
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
    if(file_format == '2'):
        ydl_opts = {
            'format': 'bestaudio/best',
            "writethumbnail": True,
            "outtmpl": "%(title)s.%(ext)s",
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                },
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

    print("\n       Download Completed...Enjoy!")


main()
