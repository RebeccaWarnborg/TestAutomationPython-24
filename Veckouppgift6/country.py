# På Island bor det 383726 invånare och i Danmark 5961249. Skapa objekt för länderna. 
# (Data från januari 2024. Avrunda befolkningen.)

# Kod ej klar.

class Country:
    def __init__(self, name, pop, area = None):
        self.__name = name
        self.__population = pop
        self.__area = area

    def __str__(self):
        return self.print_info()
    
    def print_info(self):
        return f"I {self.get_name()} bor det {self.get_population()} miljoner invånare"

    def get_name(self):
        return self.__name
    
    def get_population(self):
        return self.__population
    
    def get_area(self):
        return self.__area


se = Country("Sverige", 10.5)
no = Country("Norge", 5.5)
