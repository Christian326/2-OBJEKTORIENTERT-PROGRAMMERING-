
class Planet:
    " En klasse for å beskrive en planet"
<<<<<<< Updated upstream
    def __init__(self,navn:str,solavstand:float,radius:float,antallRinger=0) -> None:
=======
    def __init__(self,navn:str,solavstand:float,radius:float, antallRinger=0) -> None:
>>>>>>> Stashed changes

        self.navn=navn
        self.solavstand=solavstand
        self.radius = radius
<<<<<<< Updated upstream
        self.antallRinger=antallRinger

jorden = Planet( "Jorden", 152, 6371)

=======
        self.antallRinger = antallRinger

jorden = Planet( "Jorden", 152, 6371)

mars=Planet("Mars",222.9,3389.5)

jupiter = ("Jupiter", 778, 69911)

print(type(str))

#Notater
#Klassen planet
#Navn
#Radius og størrelse
#Avstand fra sola
#Antall ringer
#Farge?
#Beboelig / befolkning
#Temperatur
#++++
>>>>>>> Stashed changes

# Oppgave 1: 
# Lag et objekt for Mars, Jupiter og Jorda, der du lagrer informasjon om navn, solavstand og radius. Lagre disse objektene i egne variabler

# Hva skjer om du skriver print(Jorda)?
# Hva skjer om du skriver print(Jorda.navn)?
# Prøv å skriv ut de andre attributtene til klassen
print(jorden)
print(jorden.navn)
print(jorden.antallRinger)
# OBS: pass på rekkefølgen i argumentene til konstruktøren.



