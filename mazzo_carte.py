from random import shuffle

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