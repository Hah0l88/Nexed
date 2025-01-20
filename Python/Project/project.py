import random

# Inleiding van de game
def game():
    print("Welkom bij het spel 'Trail of Trials'!")
    print("Je bent een avonturier die de Boom van het Lot wil bereiken. Je hebt een beperkte hoeveelheid gezondheid om 15 stappen te voltooien.")

    hp = 2
    max_hp = 5
    steps = 15

    stories = [
        {
            "vraag": "Je bent een vreemd altaar tegengekomen. Wat ga je doen?",
            "antwoorden": [
                {"tekst": "Observeer het altaar van een afstand.", "effect": 0},
                {"tekst": "Leg een offer neer.", "effect": +1},
                {"tekst": "Raak het altaar aan.", "effect": -1}
            ]
        },
        {
            "vraag": "Je hoorde gefluister vanuit de schaduwen. Wat ga je doen?",
            "antwoorden": [
                {"tekst": "Negeer het gefluister en blijf op je pad.", "effect": 0},
                {"tekst": "Roep naar het geluid: 'Wie daar?!'", "effect": +1},
                {"tekst": "Loop recht op het geluid af.", "effect": -1}
            ]
        },
        {
            "vraag": "Er is een diep ravijn met een gammele brug voor je. Wat ga je doen?",
            "antwoorden": [
                {"tekst": "Zoek een alternatieve route.", "effect": 0},
                {"tekst": "Test de brug voorzichtig en steek over.", "effect": +1},
                {"tekst": "Ren de brug over.", "effect": -1}
            ]
        },
        {
            "vraag": "Je ziet een verlaten hut met een open deur. Wat ga je doen?",
            "antwoorden": [
                {"tekst": "Loop voorbij zonder naar binnen te kijken.", "effect": 0},
                {"tekst": "Onderzoek de hut.", "effect": +1},
                {"tekst": "Ga de hut binnen zonder voorzorgsmaatregelen.", "effect": -1}
            ]
        },
        {
            "vraag": "Er ligt een ondoordringbaar struikgewas in de weg. Wat doe je dan?",
            "antwoorden": [
                {"tekst": "Loop terug en zoek een andere route.", "effect": 0},
                {"tekst": "Hak een pad door het struikgewas.", "effect": +1},
                {"tekst": "Duw door het struikgewas heen.", "effect": -1}
            ]
        },
        {
            "vraag": "Je vindt een oude waterput. Zal ik op onderzoek uitgaan?",
            "antwoorden": [
                {"tekst": "Negeer de put en loop verder.", "effect": 0},
                {"tekst": "Laat een emmer zakken.", "effect": +1},
                {"tekst": "Kijk in de put zonder voorzorgsmaatregelen.", "effect": -1}
            ]
        },
        {
            "vraag": "Een woeste wolf verschijnt op je pad. Wat doe je?",
            "antwoorden": [
                {"tekst": "Blijf stil en wacht tot de wolf verdwijnt.", "effect": 0},
                {"tekst": "Schreeuw en maak jezelf groot.", "effect": +1},
                {"tekst": "Ren weg in paniek.", "effect": -1}
            ]
        },
        {
            "vraag": "Je ziet een flikkerend licht in de verte. Wat doe je?",
            "antwoorden": [
                {"tekst": "Negeer het licht en blijf op je pad.", "effect": 0},
                {"tekst": "Nader het licht voorzichtig.", "effect": +1},
                {"tekst": "Ren direct naar het licht.", "effect": -1}
            ]
        },
        {
            "vraag": "Er ligt een enorme omgevallen boom in de weg. Wat doe je?",
            "antwoorden": [
                {"tekst": "Blijf waar je bent en rust even uit.", "effect": 0},
                {"tekst": "Klim over de boom heen.", "effect": +1},
                {"tekst": "Kruip onder de boom door.", "effect": -1}
            ]
        },
        {
            "vraag": "Je ziet een vuur in de nacht. Wat doe je?",
            "antwoorden": [
                {"tekst": "Blijf op je plek en negeer het vuur.", "effect": 0},
                {"tekst": "Nader het vuur voorzichtig.", "effect": +1},
                {"tekst": "Loop rechtstreeks op het vuur af.", "effect": -1}
            ]
        },
        {
            "vraag": "Je komt een vreemde gloeiende plant tegen. Wat doe je?",
            "antwoorden": [
                {"tekst": "Observeer de plant zonder hem aan te raken.", "effect": 0},
                {"tekst": "Neem een klein monster van de plant.", "effect": +1},
                {"tekst": "Raak de plant aan.", "effect": -1}
            ]
        },
        {
            "vraag": "Er is een moeras op de weg. Wat doe je?",
            "antwoorden": [
                {"tekst": "Vermijd het moeras en zoek een langere route.", "effect": 0},
                {"tekst": "Vind een veilige doorgang door het moeras.", "effect": +1},
                {"tekst": "Loop zonder voorzorgsmaatregelen het moeras in.", "effect": -1}
            ]
        },
        {
            "vraag": "Je hoort gerommel van water. Wat doe je?",
            "antwoorden": [
                {"tekst": "Blijf op je pad en negeer het geluid.", "effect": 0},
                {"tekst": "Volg het geluid naar de rivier.", "effect": +1},
                {"tekst": "Ren naar het geluid zonder te kijken.", "effect": -1}
            ]
        },
        {
            "vraag": "Voor je staat een stenen standbeeld met een inscriptie. Wat doe je?",
            "antwoorden": [
                {"tekst": "Kijk ernaar, maar raak het niet aan.", "effect": 0},
                {"tekst": "Lees de inscriptie.", "effect": +1},
                {"tekst": "Raak het standbeeld aan.", "effect": -1}
            ]
        },
        {
            "vraag": "Je ziet een felle lichtstraal uit de lucht komen. Wat doe je?",
            "antwoorden": [
                {"tekst": "Blijf op afstand en observeer het licht.", "effect": 0},
                {"tekst": "Nader het licht voorzichtig.", "effect": +1},
                {"tekst": "Loop rechtstreeks naar het licht.", "effect": -1}
            ]
        }
    ]

    random.shuffle(stories)

    for step in range(1, steps + 1):
        if hp <= 0:
            print("Je verloor al je kracht en zakte in elkaar op het pad. Het bos heeft je opgeslokt... Het spel is uit.")
            return
    
    # Schrijft hoeveel stappen je hebt gemaakt en je huidige HP
        verhaal = stories[step - 1]
        print(f"Stap {step} van {steps}. Huidige HP: {hp}")
        print(verhaal["vraag"])
        antwoorden = verhaal["antwoorden"]
        random.shuffle(antwoorden)
    
        for i, antwoord in enumerate(antwoorden):
            print(f"{i + 1}. {antwoord['tekst']}")
    
        keuze = int(input("Maak je keuze(1/2/3):\n")) - 1
        if 0 <= keuze < len(antwoorden):  # Correcte controle
            hp += antwoorden[keuze]["effect"]  # Correct gebruik van 'antwoorden'
            hp = max(0, min(hp, max_hp))
        else:
            print("Ongeldige keuze. Het spel gaat verder.")


if __name__ == "__main__":
    game()
