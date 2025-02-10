# På Island bor det 383726 invånare och i Danmark 5961249. Skapa objekt för länderna. 
# (Data från januari 2024. Avrunda befolkningen.)

class Country:
    def __init__(self, name, pop):
        self.__name = name
        self.__population = pop

se = Country("Sverige", 10.5)
no = Country("Norge", 5.5)
