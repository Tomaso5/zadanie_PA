# obchod s elektronikou

class Produkt:
    def __init__(self, nazov, cena, sklad):
        self.nazov = nazov
        self.cena = cena
        self.sklad = sklad

    def vypis(self):
        print(f"{self.nazov} - {self.cena} € | Sklad: {self.sklad} ks")


class Elektronika(Produkt):
    def __init__(self, nazov, cena, sklad, zaruka):
        super().__init__(nazov, cena, sklad)
        self.zaruka = zaruka

    def vypis(self):
        print(f"{self.nazov} - {self.cena} € | Záruka: {self.zaruka} roky | Sklad: {self.sklad} ks")


class Obchod:
    def __init__(self):
        self.produkty = []
        self.predaje = []

    def pridaj_produkt(self, produkt):
        self.produkty.append(produkt)

    def vypis_produkty(self):
        print("Produkty v obchode:")
        for p in self.produkty:
            p.vypis()

    def predaj(self, produkt, kusy, zlava=0):
        if produkt.sklad < kusy:
            print("Nedostatok kusov na sklade")
            return

        cena_po_zlave = produkt.cena * (1 - zlava / 100)
        suma = cena_po_zlave * kusy

        produkt.sklad -= kusy
        self.predaje.append([produkt.nazov, kusy, suma])

        print(f"Predané: {produkt.nazov} | {kusy} ks | Spolu: {suma:.2f} €")

    def vypis_predaje(self):
        print("Predaje:")
        for p in self.predaje:
            print(f"Produkt: {p[0]}, Kusy: {p[1]}, Suma: {p[2]:.2f} €")

    def celkovy_obrat(self):
        obrat = 0
        for p in self.predaje:
            obrat += p[2]
        print(f"Celkový obrat obchodu: {obrat:.2f} €")


# vytvorenie produktov
p1 = Elektronika("Notebook", 900, 5, 2)
p2 = Elektronika("Myš", 25, 20, 1)
p3 = Elektronika("Monitor", 220, 10, 3)

# vytvorenie obchodu
obchod = Obchod()

# pridanie produktov
obchod.pridaj_produkt(p1)
obchod.pridaj_produkt(p2)
obchod.pridaj_produkt(p3)

# výpis produktov
obchod.vypis_produkty()

# predaje
obchod.predaj(p1, 1, zlava=10)  # 10 % zľava
obchod.predaj(p2, 4)
obchod.predaj(p3, 2)

# výpis predajov a obrat
obchod.vypis_predaje()
obchod.celkovy_obrat()
