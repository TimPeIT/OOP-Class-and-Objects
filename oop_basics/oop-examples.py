class Auto:
    def __init__(self, tankkapazität=100):
        self.tankkapazität = tankkapazität
        self.benzinstand = 0

    def tankfüllung_anzeigen(self):
        print(f"Aktueller Tankinhalt beträgt {self.benzinstand:.2f} Liter.")

    def tanken(self,liter):
        if liter <=0:
            print("Bitte Benzin tanken und keine Luft.")
            return
        neuer_stand = self.benzinstand + liter
        if neuer_stand > self.tankkapazität:
            übertankung = neuer_stand - self.tankkapazität
            self.benzinstand = neuer_stand
            print(f"Tank voll! {übertankung:.2f} Liter konnten nicht getankt werden.")
        else:
            self.benzinstand = neuer_stand
            print(f"{liter:.2f} Liter getankt.")

    def fahren(self, kilometer, verbrauch_pro_100km=7):
        if kilometer <= 0:
            print("Bitte positive Kilometer eingeben.")
            return
        benötigter_sprit = (verbrauch_pro_100km / 100) * kilometer
        if benötigter_sprit > self.benzinstand:
            print("Nicht genug Benzin!")
        else:
            self.benzinstand -= benötigter_sprit
            print(f"Auto ist {kilometer} gefahren und verbraucht {benötigter_sprit:.2f} Liter.")

auto = Auto()
auto.tankfüllung_anzeigen()
auto.tanken(80)
auto.tankfüllung_anzeigen()
auto.tanken(20)
auto.tankfüllung_anzeigen()
auto.fahren(550)
auto.tankfüllung_anzeigen()