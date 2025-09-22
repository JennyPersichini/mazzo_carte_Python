class Carta():
    def __init__(self, valore, seme):
        self.valore = valore
        self.seme = seme

    def __repr__(self):
        return f"{self.valore} di {self.seme}"

c = Carta("A", "Spade")
print(c)