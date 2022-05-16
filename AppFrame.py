from tkinter import Tk, Label, Button, W, E
from tkinter.ttk import Frame, Style
from random import choice
import main as main

class AppFrame(Frame):
    isStart = False
    isWord = False
    los = 0

    def initGui(self):
        self.title("DLLAP")
        #App.state('zoomed')
        # App.geometry("600x400")
        #App.config(background="#505050")

        Style().configure("Interface", padding=(0, 5, 0, 5), font=("Calibri 80 bold"))

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)

        #self.bind("<Key>", self.key_pressed)

        self.word = Label(self, text="", font=("Calibri 80 bold"), fg="#FFFFFF", background="#505050")
        self.word.grid(row=1,columnspan=3)
        self.definition = Label(self, text="", font=("Calibri 80 bold"), fg="#FFFFFF", background="#505050")
        self.definition.grid(row=2,columnspan=3)
        #self.word.pack()
        #self.definition.pack()

        #learn = Button(self, text="Start", font="Calibri 20 bold", fg="#505050", command=lambda: self.startLearning())
        #learn.pack()

        self.pack()

    def startLearning(self):
        self.isStart = True
        self.goFurther()

    def goFurther(self):

        if (self.isStart==True):

            if self.isWord == False:
                self.word.config(text="")
                self.definition.config(text="")
                self.los = choice(range(len(main.r.decks.get(main.name))))
                print(len(main.r.decks.get(main.name)))
                newWord = main.r.decks.get(main.name)[self.los].get("Word")
                self.word.config(text=newWord)
                self.isWord = True

            elif self.isWord == True:

                newDef = main.r.decks.get(main.name)[self.los].get("Def")
                self.definition.config(text=newDef)
                self.isWord = False


    def key_pressed(self, event):

        if (self.isStart==True):
            if(event.char==" "):
                self.goFurther()
            elif (event.char=="1"):
                self.goFurther()
            elif (event.char=="2"):
                self.goFurther()

    def __init__(self):
        super().__init__()

        self.initGUI()