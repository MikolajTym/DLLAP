from tkinter import Tk, Label, Button
from random import choice
import main as main

class AppFrame():
    isDef = False
    word = Label
    definition = Label

    def startLearning(self):
        los=0
        if self.isDef == False:
            self.word.config(text="")
            self.definition.config(text="")
            los = choice(range(len(main.r.decks.get("english2"))))
            newWord = main.r.decks.get("english2")[los].get("Word")
            self.newDef=main.r.decks.get("english2")[los].get("Def")
            self.word.config(text=newWord)
            self.isDef = True

        elif self.isDef==True:

            self.definition.config(self,text=self.newDef)
            self.isDef = False
            main.r.decks.get("english2").pop(los)

    def key_pressed(self,event):
        if(event.char==" "):
            #self.startLearning()
            pass

    def __init__(self):
        App = Tk()
        App.title("DLLAP")
        App.geometry("600x400")
        App.config(background="#505050")

        word = Label(App, text="", font=50, fg="#000000",background="#505050")
        definition = Label(App, text="", font=50, fg="#000000",background="#505050")

        App.bind("<Key>",self.key_pressed)

        word.pack()
        definition.pack()

        learn = Button(App, text="Start", font=50, fg="#505050", command=lambda: self.startLearning(self))
        learn.pack()

        App.mainloop()



