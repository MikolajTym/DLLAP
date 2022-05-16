from tkinter import Label, Button, RIGHT, LEFT, BOTH, RAISED, messagebox
from tkinter.ttk import Frame, Style
from random import choice

import main as main
import reader as reader

name = "First Meeting"
r=reader.reader(name)

class AppFrame(Frame):
    isStart = False
    isWord = False
    isDef = False
    los = 0

    def initGUI(self):

        self.master.title("DLLAP")
        self.master.state('zoomed')
        self.style = Style()
        self.style.theme_use("default")

        self.word = Label(self, text="W1", font=("Calibri 80 bold"), fg="#FFFFFF", background="#505050")
        self.word.pack(fill=BOTH, expand=True)

        self.definition = Label(self, text="W2", font=("Calibri 80 bold"), fg="#FFFFFF", background="#505050")
        self.definition.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)

        learn = Button(self, text="Start", font="Calibri 20 bold", fg="#505050", command=lambda: self.startLearning(),padx=50)
        learn.pack(side=RIGHT)

        self.master.bind("<Key>", self.key_pressed)

    def startLearning(self):

        if self.isStart==False:
            r = reader.reader(name)

        self.isStart = True
        self.goFurther()

    def goFurther(self):

        if (self.isStart==True and len(r.decks.get(name))!=0):

            self.isDef = False

            if self.isWord == False:
                self.word.config(text="")
                self.definition.config(text="")
                self.los = choice(range(len(r.decks.get(name))))
                newWord = r.decks.get(name)[self.los].get("Word")
                self.word.config(text=newWord)
                self.isWord = True

            elif self.isWord == True:

                newDef = r.decks.get(name)[self.los].get("Def")
                self.definition.config(text=newDef)
                self.isDef = True
                self.isWord = False

    def removeWord(self):

        if len(r.decks.get(name))==0:
            messagebox.showinfo("Congratulations!", "You have learned all the words!")
            self.endLearning()
        else:
            if self.isDef==True:
                r.decks.get(name).pop(self.los)

    def endLearning(self):
        self.isStart=False
        self.word.config(text="")
        self.definition.config(text="")

    def key_pressed(self, event):

        if (self.isStart==True):
            if(event.char==" "):
                self.goFurther()
            elif (event.char=="1"):
                self.goFurther()
            elif (event.char=="2"):
                self.removeWord()
                self.goFurther()

    def __init__(self):
        super().__init__()

        self.initGUI()