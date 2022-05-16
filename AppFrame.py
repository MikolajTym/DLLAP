from tkinter import Tk, Label, Button
from random import choice
import main as main

class AppFrame():
    isDef = False
    word = Label
    definition = Label

    def startLearning(self, word, definition):
        los=0
        if self.isDef == False:
            word.config(text="")
            definition.config(text="")
            los = choice(range(len(main.r.decks.get("english2"))))
            newWord = main.r.decks.get("english2")[los].get("Word")
            self.newDef=main.r.decks.get("english2")[los].get("Def")
            word.config(text=newWord)
            self.isDef = True

        elif self.isDef==True:

            definition.config(text=self.newDef)
            self.isDef = False
            #main.r.decks.get("english2").pop(los)

    def key_pressed(self,event):
        if(event.char==" "):
            #self.startLearning() # TODO DOESNT WORKING
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

        learn = Button(App, text="Start", font=50, fg="#505050", command=lambda: self.startLearning(word, definition))
        learn.pack()

        App.mainloop()



