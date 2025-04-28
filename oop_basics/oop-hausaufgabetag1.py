class Produkt:
    def __init__(self, name, preis, bestand):
        self.name = name
        self.preis = preis
        self.bestand = bestand

    def produkt(self):
        print(f"Das Produkt {self.name} hat den Preis von {self.preis:.2f}, es sind noch {self.bestand} im Bestand.")
    
    def kaufen(self, gekauft=1):
        if gekauft <= self.bestand:
            self.bestand -= gekauft
            print(f"{gekauft} Stück von {self.name} gekauft.")
        else:
            print(f"Nicht genügend auf Lager von {self.name}")
    
    def preis_ändern(self, neuer_preis):
        if neuer_preis >= 0:
            self.preis = neuer_preis
            print(f"Neuer Preis von {self.name} ist {self.preis}.")
        else:
            print("Es gibt keine negativen Preise")
        
    def __str__(self):
        return f"Produkt: {self.name}, Preis: {self.preis:.2f}, Bestand: {self.bestand}"


p = Produkt("Monitor", 249.99, 4)
p1 = Produkt("Teeservice", 69.99, 10)
p.kaufen(1)
p.preis_ändern(229.99)
print(p)
p.kaufen(5)