import random

# Inleiding van de game
def game():
    print("Welkom bij het spel 'Trail of Trials'!")
    print("Je bent een avonturier die de Boom van het Lot wil bereiken. Je hebt een beperkte hoeveelheid gezondheid om 15 stappen te voltooien.")

    hp = 2
    max_hp = 5
    step = 15

    stories = [
        "Je bent een vreemd altaar tegengekomen. Wat ga je doen?"
        "Je hoorde gefluister vanuit de schaduwen. Het zou een geest kunnen zijn. Wat ga je doen?"
        "Er is een diep ravijn met een gammele brug voor je. Wat ga je doen?"
        "Je ziet een verlaten hut met een open deur. “Wat ga je doen?"
        "Er ligt een ondoordringbaar struikgewas in de weg. Je kunt proberen er omheen te gaan. “Wat doe je dan?"
        "Je vindt een oude waterput. Er kan iets van waarde in zitten. Zal ik op onderzoek uitgaan?"
        "Een woeste wolf verschijnt op je pad. Moet je proberen te ontwijken of jezelf verdedigen?
        "Je ziet een flikkerend licht in de verte. Het kan een redding zijn of een valstrik. Wat moet je doen?
        "Er ligt een enorme omgevallen boom in de weg. Moet ik er overheen klimmen of er omheen gaan?
        "Je ziet een vuur in de nacht. Het zouden andere reizigers kunnen zijn. “Moeten we het controleren?
        "Je komt een vreemde gloeiende plant tegen. “Wat ga je doen?
        "Er is een moeras op de weg. Het lijkt gevaarlijk, maar een kortere weg. Ga je er doorheen?”
        "Je hoort gerommel van water. Misschien is er verderop een rivier. Zullen we proberen een doorwaadbare plaats te vinden?”
        "Voor je staat een stenen standbeeld met een inscriptie. “Moet je het lezen?
        "Je ziet een felle lichtstraal uit de lucht komen. Moet ik deze plek controleren?”
    ]
