from random import choice
from tkinter import Tk
import reader as r
import AppFrame as app

name="english2"
r = r.reader(name)

if __name__ == '__main__':
    # dictionary_name.get(name, value)

    App = Tk()
    app = app.AppFrame()
    App.mainloop()
