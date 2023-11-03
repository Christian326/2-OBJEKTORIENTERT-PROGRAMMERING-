# Løsning av oppgave 1.md
class Person:
    """
    Klasse for å lage planet-objekter.
    Parametre:
    fornavn (str): Personens fornavn
    etternavn (str): Personens etternavn
    fødselsår (int): Personens fødselsår
    """
    def __init__(self, fornavn:str, etternavn:str, fødselsår:int)->None:
        """ Konstruktør """
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fødselsår = fødselsår
    
    def beregnAlder(self, årstall:int)->int:
        """ Metode som beregner personens alder """
        return årstall - self.fødselsår
    
    def visInfo(self, årstall:int)->None:
        """ Metode som skriver ut informasjon om personen """
        print(f"{self.fornavn} {self.etternavn} er {self.beregnAlder(årstall)} år gammel.") 

# Test av personklassen:
p1 = Person("Ola", "Olasen", 1994) 
p2 = Person("Kari", "Karinen", 1998) 
p1.visInfo(2022) 
p2.visInfo(2022) 

class Elev(Person):
    """
    Klasse for å lage elev-objekter.
    Parametre:
    fornavn (str): Personens fornavn
    etternavn (str): Personens etternavn
    fødselsår (int): Året personen ble født
    """
    def __init__(self, fornavn: str, etternavn: str, fødselsår: int)->None:
        super().__init__(fornavn, etternavn, fødselsår)

    def finnTrinn(self)->str:
        """ Metoden finner elevens trinn """
        # Metoden må justeres for det aktuelle årskullet
        if (self.fødselsår == 2003):
            return "Vg3"
        elif (self.fødselsår == 2004):
            return "Vg2"
        elif (self.fødselsår == 2005):
            return "Vg1"
        else: 
            return "ukjent trinn"
        
    def visInfo(self, årstall)->None:
        """ Metoden skriver ut informasjon om eleven """
        print(f"{self.fornavn} {self.etternavn} er {self.beregnAlder(årstall)} år gammel og går i {self.finnTrinn()}.") 

# Test av Elev-klassen
elev1 = Elev("Jesper", "Nattmann", 2004) 
elev2 = Elev("Mia", "Morgenfugl", 2003) 
elev3 = Elev("Fredrik", "Formiddagsbjørn", 2005) 
elev1.visInfo(2022) 
elev2.visInfo(2022) 
elev3.visInfo(2022) 


class Lærer(Person):
    """
    Klasse for å lage lærer-objekter.
    Parametre:
    fornavn (str): Personens fornavn
    etternavn (str): Personens etternavn
    fødselsår (int): Året personen ble født
    fag (list): Liste over fagene læreren kan undervise i
    kontaktklasse (str): Klassen læreren ev. er kontaktlærer for
    """
    def __init__(self, fornavn: str, etternavn: str, fødselsår: int, fag: list, kontaktklasse: str = "")->None:
        super().__init__(fornavn, etternavn, fødselsår)
        self.fag = fag
        self.kontaktklasse = kontaktklasse
        
    def sjekkfag(self, fagnavn: str)->bool:
        """ Metoden sjekker om læreren underviser i et gitt fag """
        return fagnavn in self.fag
    
    def visInfo(self, årstall:int)->None:
        """ Metoden skriver ut informasjon om læreren """
        super().visInfo(årstall)
        if (len(self.fag) > 0):
            fagtekst = f"{self.fornavn} "
            if (self.kontaktklasse != ""):
                fagtekst += f"er kontaktlærer for {self.kontaktklasse} og "
            fagtekst += "underviser i "
            n = len(self.fag)
            for i in range(n):
                if (i == n-1):
                    fagtekst += " og "
                elif (i > 0):
                    fagtekst += ", "
                fagtekst += f"{self.fag[i]}"

            print(fagtekst)
# Test av Lærer-klassen
Lærer1 = Lærer("Hans", "Vie", 1995, ["Matematikk", "Naturfag","Fysikk", "IT","Biologi","Kjemi"], "") 
Lærer1.visInfo(2022) 
print(Lærer1.sjekkfag("Engelsk"))
print(Lærer1.sjekkfag("Matematikk"))

