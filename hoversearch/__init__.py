#! /usr/bin/python3
import sys
import json
import os
import shutil
try:
    import urllib3
except ImportError:
    os.system('cmd /k "pip install urllib3"')
try:
    import bs4
except ImportError:
    os.system('cmd /k "pip install bs4"')
try:
    import requests
except ImportError:
    os.system('cmd /k "pip install requests"')
try:
    import asyncio
except ImportError:
    os.system('cmd /k "pip install asyncio"')
try:
    import youtube_dl
except ImportError:
    os.system('cmd /k "pip install youtube-dl"')
try:
    import ffmpeg
except ImportError:
    os.system('cmd /k "pip install ffmpeg"')
defaultydl_opts = {'format': 'bestaudio/best','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp4','preferredquality': '192',}],}
class Youtube():
    def search(self, type="url", search=None, download=None, downloadformat="mp4", destination="./", ydl_opts=None):
        fullcontent = ('http://www.youtube.com/results?search_query=' + search)
        text = requests.get(fullcontent).text
        soup = bs4.BeautifulSoup(text, 'html.parser')
        img = str(soup.find_all('img')[9]["src"])
        div = [ d for d in soup.find_all('div') if d.has_attr('class') and 'yt-lockup-dismissable' in d['class']]
        a = [ x for x in div[0].find_all('a') if x.has_attr('title')]
        title = (a[0]['title'])
        a0 = [ x for x in div[0].find_all('a') if x.has_attr('title') ][0]
        url = ('http://www.youtube.com'+a0['href'])
        if ydl_opts is None:
            if downloadformat == "mp4":
                ydl_opts = {'format': 'bestaudio/best','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp4','preferredquality': '192',}],}
        if search is None:
            print("Nothing to search:", sys.exc_info()[0])
            raise
        if download is None or download == "False":
            if type == "url":
                return url
            if type == "title":
                return title
            if type == 'search':
                return search
        if download == "True":
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                videoformat = str(downloadformat)
                for file in os.listdir("./"):
                    if file.endswith(".mp4"):
                        if destination == "./":
                            pass
                        if destination != "./":
                            print(title)
                            filename = str(title) + "." + str(videoformat)
                            os.rename(file, filename)
                            file = title + "." + downloadformat
                            try:
                                shutil.move(file, r"{}".format(destination))
                            except FileExistsError:
                                print("File already exists:", sys.exc_info()[0])
                                raise

    

if __name__ == "__main__":
    exit()
