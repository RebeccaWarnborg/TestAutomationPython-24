# Bygg ett program där användaren kan lägga till saker till en todo-lista.

todo_list = []

def visa_meny():
    print("** Todo list extravaganza **")
    print("1. Se innehållet i din lista")
    print("2. Lägga till nya punkter i din lista")

def huvudprogram():
    while True:
        visa_meny()
        val = input("Välj ett alternativ: ")

        # Alternativ 1: Se innehållet i listan
        if val == "1":
            if len(todo_list) == 0:
                print("Din lista är tom.")
            else:
                print("\nDin todo-lista:")
                for item in todo_list:
                    print(f"+ {item}")

        # Alternativ 2: Lägga till en ny punkt
        elif val == "2":
            ny_punkt = input("Skriv in en ny sak du måste komma ihåg att göra: ")
            todo_list.append(ny_punkt)  # Lägger till punkten i listan
            print(f"Ok, lade till \"{ny_punkt}\" i listan.")

        # Hantera ogiltiga val
        else:
            print("Ogiltigt val, försök igen.")

# Anropa huvudprogram för att köra programmet
huvudprogram()