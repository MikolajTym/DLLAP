class reader:

    deck =[]

    def __init__(self, name):

        file = open("Deck/"+name+".txt", encoding="utf-8")
        for line in file:
            global deck
            deck.append(line)

        file.close()