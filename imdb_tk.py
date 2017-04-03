import json
from urllib.request import urlopen
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import re
movie_name = ''
def GUI():
    root = Tk()
    root.geometry("800x500")
    L1 = Label(root, text="Enter the movie ?")
    L1.pack(side=LEFT)
    E1 = Entry(root, bd=10)
    def helloCallBack():
        movie_name = E1.get()
        m = MOVIE_JSON(movie_name)
        msg = messagebox.showinfo("IMDB Info","\nTitle\t\t"+m["Title"]+"\nYear\t\t"+m["Year"]+"\nReleased\t\t"+m["Released"]+"\nRuntime\t\t"+m["Runtime"]+"\nGenre\t\t" + m["Genre"] + "\nDirector\t\t" + m["Director"] + "\nActors\t\t" + m["Actors"]+"\n\nPlot\n" + m["Plot"])

    B = Button(root, text="Submit", command=helloCallBack)
    E1.pack(side=RIGHT)
    B.place(x=700, y=300)
    root.mainloop()

def MOVIE_JSON(movie_name):
    url = "http://www.omdbapi.com/?t="+movie_name+"&y=&plot=short&r=json"
    my_info = urlopen(url).read().decode('utf8')
    h = json.loads(my_info)
    return h
if __name__ == "__main__":
    GUI()