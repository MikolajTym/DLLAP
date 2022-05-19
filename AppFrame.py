from tkinter import Label, Button, RIGHT, LEFT, BOTH, RAISED, messagebox
from tkinter.ttk import Frame, Style
from random import choice

from gtts import gTTS # Text to speech conversion
from playsound import playsound

import reader as reader

name = "First Meeting"
r=reader.reader(name)

class AppFrame(Frame):
    isStart = False
    isWord = False
    isDef = False
    los = 0
    fontSize = 180
    screen_width=1920
    sizeWord = 0
    #screen_width = self.winfo_screenwidth()
    #screen_height = self.winfo_screenheight()


    def changeSizeOfFont(self, label, size):

        while (size>(self.screen_width-50)): # TODO WIDTH NIE DZIAŁA
            self.fontSize-=10
            print(str(size)+" > "+str(self.screen_width-50))
            print(self.fontSize)

        label.config(font=(f"Calibri {self.fontSize} bold"))

        self.fontSize=180


    def initGUI(self):

        self.master.title("DLLAP")
        self.master.state('zoomed')
        self.style = Style()
        self.style.theme_use("default")

        self.word = Label(self, text="", font=(f"Calibri {self.fontSize} bold"), fg="#FFFFFF", background="#505050")
        self.word.pack(expand=True)

        self.definition = Label(self, text="", font=(f"Calibri {self.fontSize} bold"), fg="#FFFFFF", background="#505050")
        self.definition.pack(expand=True)

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
                self.word.config(text=newWord, font=(f"Calibri {self.fontSize} bold"))


                #speech = gTTS(text=newWord, lang="en", slow=False)
                #speech.save("speech.mp3")
                #playsound("speech.mp3")

                #self.changeSizeOfFont(self.word)

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
                self.sizeWord=self.definition.winfo_width()
                self.changeSizeOfFont(self.definition, self.sizeWord)
            elif (event.char=="1"):
                self.goFurther()
            elif (event.char=="2"):
                self.removeWord()
                self.goFurther()

    def __init__(self):
        super().__init__()

        self.initGUI()
