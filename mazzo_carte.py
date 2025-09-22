from random import shuffle

class Mazzo():
    def __init__(self):
        semi = ["Bastoni", "Coppe", "Denari", "Spade"]
        valori = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

        self.carte = [Carta(valore, seme) for seme in semi for valore in valori]

    def conta(self):
        return len(self.carte)

    def __repr__(self):
        return f"Mazzo di {self.conta} carte"

