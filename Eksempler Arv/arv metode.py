class Rektangel:
    """Klasse for å representere et rektangel"""
    def __init__(self, lengde, bredde):
        """Konstruktør"""
        self.lengde = lengde
        self.bredde = bredde
    
    def areal(self):
        """Metode for å beregne areal"""
        return self.lengde * self.bredde

    def info(self):
        """Metode som skriver ut informasjon om rektangelet"""
        print(f" Lengde:{self.lengde:.2f}, Bredde: {self.bredde:.2f}, Areal: {self.areal():.2f}, Type: {type(self)}")

class Kvadrat(Rektangel):
    """Klasse for å representere et kvadrat"""
    def __init__(self, sidekant):
        super().__init__(sidekant, sidekant)

    def info(self):
        print(f" Sidelengde:{self.lengde:.2f}, Areal: {self.areal():.2f}, Type: {type(self)}")

kvadrat1 = Kvadrat(2)
rektangel1 = Rektangel(2, 3)

rektangel1.info()
kvadrat1.info()
