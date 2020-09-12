"""
Titel voor je avontuur: De queeste naar taart.

Opmerkingen over hoe je het avontuuur kan "winnen" of "verliezen":
* kies de tafel om te winnen
* kies de deur om te verliezen
"""

import time

def bloem ():   
    delay = 0.0

    soort = input ("Wat leuk! Je mag een bloetje uitkiezen! Welke soort bloem zou je het liefst willen hebben? [hibiscus/roos/tulp]")
    if soort == "hibiscus":
        print()
        print ("Mooie soort!")
    elif soort == "roos":
        print()
        print ("Leuk! Ze prikken alleen altijd zo!")
    else:
        print()
        print ("Een leuke keus!")

    kleur = input("Je mag nu de kleur uitkiezen, welke kleur vind je leuk? [Geel/Rood/Wit/Anders] ")
    print ()

    if kleur == "geel":
        print()
        print("Geel is een hele mooie kleur! De kleur van de zon, bijtjes, bananen, en nu ook je bloem!")
    elif kleur == "wit":
        print ()
        print ("Wit is altijd zo wit, als het vies is zie je het meteen, maar gelukkig is dat bij bloemen niet zo. \
            Die worden niet zo snel vies.")
    elif kleur == "rood":
        print()
        print ("Vandaag is rood, de kleur van mijn.. bloem!")
    else:
        print()
        print ("Eigenlijk is elke kleur wel mooi bij deze bloem.")


    naam = input("Gefeliciteerd! Je hebt een bloem gekregen. Hoe ga je hem noemen?")
    print()

    if naam == "bloem":
        print ()
        print("Lekker origineel!") 

    print ()
    print ("Je hebt nu een bloemetje, je hebt hem", naam, "genoemd.")  
    print ("Je moet hem nu gaan verzorgen.") 
    verzorging = input ("Wat wil je gaan doen? [neerzetten/water]")
    if verzorging == "neerzetten":
        print()
        print ("Je hebt hem nu op de vensterbank gezet.")
        print ("Hij staat daar heel mooi.")
    elif verzorging == "water":
        print ()
        print ("Een bloem water geven is belangrijk!")
        print ("Gelukkig heeft hij nu water gehad.")
    
    print ()
    print ("Leuk dat je blij bent met je bloem")
    print ("Je bloemetje blijft maar groeien en bloeien")
    print ("Een paar dagen later merk je op dat er luis op je bloem zit!")
    print ("Wat een ramp!")
    uitkomst = input("Wat ga je nu doen? [bestrijden/niks] ")
    if uitkomst == "bestrijden":
        print ()
        print ("Je hebt je plant gered van de dood!")
        print ("Die beesten konden je plant helemaal opeten!")
        print ("Gelukkig is dat niet gebeurd!")
        print ("Je bloem leefde nog lang en gelukkig!")
    else:
        print()
        print ("Hoe kon je niks doen!?")
        print ("Nadat je zo lang voor je bloem hebt gezorgd!")
        print ("Nu issie dood :(")
        print ("Misschien moet je de volgende keer het wel bestrijden")
    
    print ("Je had je bloem", naam,"genoemd, hij was een", soort,"in de kleur", kleur,".")
    print ("Het was een mooie bloem.")