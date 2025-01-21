movies = ["The nun", "The conjuring", "Anabelle", "The Exorcism"]
movies.append("Fellowship of the ring")
movies.insert(0,"The two towers")
movies.remove("The nun")
print("Skräckfilmer: ")
for movie in movies:
    print("- ", movie)

print("Filmen Fellowship of the ring har plats:",movies.index("Fellowship of the ring"))


