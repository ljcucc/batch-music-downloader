from __future__ import unicode_literals
from youtubesearchpython import VideosSearch

import youtube_dl

import csv
import random

def readCSV():
    music_list = []
    with open("./workspace/music_list.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for rows in reader:
            data = {}

            for key in rows.keys():
                data[key] = rows[key]
            music_list.append(data)
    
    return music_list

def countSec(time):
    print(f"LOG: {time}")
    if(not len(time.split(":")) == 2):
        print("over then 1 hour...")
        return -1
    m, s = time.split(":")
    return int(s) + (int(m) * 60)

def search(title, dur, info = {}):
    vsearch = VideosSearch(f'{title} {info["album"]} music', limit = 5)
    result = vsearch.result()

    final = []
    
    for item in result["result"]:
        print("-"*20)
        print(f'time: {item["duration"]} -> {countSec(item["duration"])}')
        print(item["type"])

        data = {
            "origin": item,
            "dur_count": dur - countSec(item["duration"])
        }

        final.append(data)
    
    return final

def sortSearch(l):
    def sortFunc(item):
        return item["dur_count"]
    
    l.sort(key=sortFunc)

    return l

def download(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    print("starting...")
    data = readCSV()
    sample = data[random.randint(0, len(data) - 1)]

    print(sample)

    dur = (countSec(sample["time"]))
    print(dur)

    finalResult = search(sample["title"], dur, info=sample)
    finalResult = sortSearch(finalResult)

    print(finalResult[0])

    url = finalResult[0]["origin"]["link"]
    # download(url)
    

if __name__ == "__main__":
    main()
