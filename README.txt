ISTRUZIONI

Creare due classi: Carta e Mazzo

Per la classe Carta:
    - Ogni istanza deve avere un seme ("Bastoni", "Coppe", "Denari" e "Spade")
    - Ogni istanza deve avere un valore("A", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    - dunder method repr deve restituire il valore della carta e il suo seme ("2 di Denari", "A di Bastoni", ..)

Per la classe Mazzo:
    - ogni istanza deve avere un attributo con tutte le possibili 40 combinazioni delle istanze della classe Carta
    - un metodo di istanza conta che deve restituire il numero delle carte rimanenti nel mazzo
    - Dunder method repr che deve restituire informazioni su quante carte sono rimaste nel mazzo ( "Mazzo di 40 carte", "Mazzo di 5 carte", ...)
    - Un metodo protetto di istanza chiamato _distribuisci che accetta un numero e rimuove quel numero di carte dal mazzo (fai attenzione a considerare i casi in cui provi a rimuovere più carte di quelle rimaste del mazzo). Se nel mazzo sono rimaste 0 carte e provi a rimuovere delle carte, questo metodo deve restituire un ValueError con il messaggio: "Non ci sono più carte nel mazzo"
    - un metodo di istanza chiamato mischia che deve mischiare (usa la funzione shuffle di random) il mazzo di carte e restituire il mazzo di carte mischiato, ma solo se questo ha tutte le 40 carte, altrimenti se alcune carte sono state già distribuite, se provi a chiamare questo metodo, devi lanciare una eccezione, un ValueError con il messaggio: "Posso mischiare solo il mazzo con tutte le carte"
    - Un metodo di istanza distribuisci_carta che sfrutta il metodo distribuisci per distribuire una carta dal mazzo e restituire quella carta
    - Un metodo di istanza distribuisci_mano che riceve un numero come parametro e sfrutta il metodo distribuisci per distribuire un numero di carte dal mazzo e restituire la lista delle carte distribuite