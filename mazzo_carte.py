from random import shuffle

class Carta():
    def __init__(self,)

class Mazzo():
    def __init__(self):
        semi = ["Bastoni", "Coppe", "Denari", "Spade"]
        valori = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

        self.carte = [Carta(valore, seme) for seme in semi for valore in valori]

    def conta(self):
        return len(self.carte)

    def __repr__(self):
        return f"Mazzo di {self.conta} carte"

    def _distribuisci(self,num):
        count = self.conta()
        n_carte_da_distribuire = min([count,num])
        if count == 0:
            raise ValueError("Non ci sono più carte nel mazzo")
        self.carte = self.carte[:-n_carte_da_distribuire]
        carte = self.carte[-n_carte_da_distribuire:]
        return carte
    
    def mischia(self):
        if self.conta() < 40:
            raise ValueError("Posso mischiare solo il mazzo con tutte le carte")
        shuffle(self.carte)

    def distribuisci_carta(self):
        return self._distribuisci(1)[0]
    
    def distribuisci_mano(self,num):
        return self._distribuisci(num)
    
d = Mazzo()
print(d.carte)
d.mischia()
print(d.carte)
carta = d.distribuisci_carta()
print(carta)
mano = d.distribuisci_mano(5)
print(mano)