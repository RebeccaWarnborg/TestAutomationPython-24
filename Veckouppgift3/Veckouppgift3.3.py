movies = ["The nun", "The conjuring", "Anabelle", "The Exorcism"]

# Lägg till "Fellowship of the ring" sist i listan.
movies.append("Fellowship of the ring")

# Lägg till "The two towers" på första platsen i listan
movies.insert(0,"The two towers")

# Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
movies.remove("The nun")
print("Skräckfilmer: ")
for movie in movies:
    print("- ", movie)

#  Ta reda på vilken position (index) "Fellowship of the ring" har
print("Filmen Fellowship of the ring har plats:",movies.index("Fellowship of the ring"))

# Ta reda på hur lång listan är


