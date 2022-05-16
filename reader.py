class reader:

    decks = {}

    def __init__(self, name):

        file = open("Deck/"+name+".txt", encoding="utf-8")
        deck=[]
        word=""
        definition=""

        for i,line in enumerate(file):

            line=line.replace('\n','')

            if ((i+2)%2==0):
                # ENGLISH
                word=line
            else:
                # POLISH
                definition=line
                deck.append({"Word" : word,"Def" :definition})

        self.decks[name]=deck

        file.close()