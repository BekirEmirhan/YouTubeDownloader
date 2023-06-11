from pytube import YouTube
import tkinter as tk
import os

global window,opt
def callback(*args):
    global yt,options_list,window,opt
    link = ytI.get()
    resList = []
    if len(link)>20:
        yt = YouTube(link)
        streams = yt.streams.order_by("resolution")
        for s in streams:
            resList.append(str(s.resolution)) 
    resList = list(set(resList))
    resList.sort()
    valIn.set("Choose Resolution")
    opt['menu'].delete(0, 'end')
    for r in resList:
        opt['menu'].add_command(label=r, command=tk._setit(valIn, r))

def download():
    global window,yt
    
    res = valIn.get()
    control = valIn2.get()
    
    
    title = yt.title
    
    if control == "mp3":
        mp3_files = yt.streams.filter(only_audio=True).first()
        mp3_files.download("music")
        base, ext = os.path.splitext(r"music\\" + yt.title + ".mp4")
        new_file = base + '.mp3'
        os.rename(r"music\\" + yt.title + ".mp4", new_file)
    else:
        try:
            print(yt.streams)
            mp4_files = yt.streams.filter(resolution=res)
            mp4_files[0].download("video")
            lblErr.place_forget()
        except:
            errorText.set("This video has not " + res + " resolution!")
            lblErr.place(x=150,y=150)
        #print(type(mp4_files[0]))
        #mp4_369p_files = mp4_files.
        #mp4_369p_files.download("video")
window = tk.Tk()
window.geometry("500x300")
window.configure(bg="#7F7FFF")
window.title("YouTube Downloader")



photo = tk.PhotoImage(file = "icon")
window.iconphoto(False, photo)


linkEnt = tk.StringVar(window)
linkEnt.trace("w",callback)
ytI = tk.Entry(window,width=45,textvariable=linkEnt)
ytI.place(x=50,y=200) 
ytI.configure(border=5,fg="#0000CD")


btnYt = tk.Button(window,command=download,text="Download")
btnYt.place(x=375, y=200)
btnYt.configure(bg="red",border=5)


lbl = tk.Label(text="YouTube\n                  Downloader",font=("Impact", 25))
lbl.place(x=70,y=50)
lbl.configure(bg="#7F7FFF")
valIn = tk.StringVar(window)
valIn.set("Choose Resolution")
options_list = ["360p", "480p", "720p", "1080p"]


valIn2 = tk.StringVar(window)
valIn2.set("Choose Format")
options_list2 = ["mp3", "mp4"]

opt = tk.OptionMenu(window,valIn,*options_list)
opt.configure(width=15)
opt.place(x=340,y=250)

opt2 = tk.OptionMenu(window,valIn2,*options_list2)
opt2.configure(width=15)
opt2.place(x=200,y=250)

errorText = tk.StringVar(window)

lblErr = tk.Label(textvariable = errorText)
lblErr.configure(bg="#7F7FFF",font=("Impact", 12))
lblErr.place(x=150,y=150)
lblErr.place_forget()
onur


tk.mainloop()
