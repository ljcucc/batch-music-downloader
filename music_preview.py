import requests
import base64
import json

import tkinter as tk
from PIL import Image,ImageTk

def open_preview(music, origin):
    print("opening... ")
    music = music["origin"]
    print(json.dumps(music))
    print(music["thumbnails"][0]["url"])

    app = tk.Tk()
    app.title("Music Preview Window")

    url = music["thumbnails"][0]["url"] 
    im = Image.open(requests.get(url, stream=True).raw)
    test = ImageTk.PhotoImage(im)

    musicTitle = tk.Label(text=f'origin "{origin["title"]}" ➡️ YT "{music["title"]}"')
    musicTitle.pack()

    imageWid = tk.Label(image=test)
    imageWid.image = test
    imageWid.pack()

    app.mainloop()