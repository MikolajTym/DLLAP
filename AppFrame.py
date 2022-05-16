from tkinter import Tk, Label, Button
import reader as r


def startLearning(word):
    #reader=r.reader("english2")
    word.config(text=r.deck[3])

class AppFrame:

    def __init__(self):
        App = Tk()
        App.title("DLLAP")
        App.geometry("600x400")
        App.config(background="#505050")

        word = Label(App, text="", font=50, fg="#000000",background="#505050")
        definition = Label(App, text="", font=50, fg="#000000",background="#505050")

        definition.pack()
        word.pack()

        learn = Button(App, text="Start", font=50, fg="#505050", command=lambda: startLearning(word))
        learn.pack()

        App.mainloop()
