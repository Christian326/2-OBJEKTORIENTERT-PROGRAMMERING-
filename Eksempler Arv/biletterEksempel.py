class Billett():
    def __init__(self):
        self.mva = 0.12
        self.pris = 20

    def beregnPris(self):
        return self.pris + (self.pris * self.mva)
  

class Barnebillett1(Billett):
    def __init__(self):
        super().__init__()
        self.rabatt = 0.5
    
    def beregnPris(self):
        rabattpris = self.pris * self.rabatt
        return rabattpris + (rabattpris * self.mva)

class Barnebillett2(Billett):
    def __init__(self):
        super().__init__()
        self.rabatt = 0.5

    def beregnPris(self):
        return super().beregnPris() * self.rabatt