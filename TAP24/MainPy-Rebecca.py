 print('Hello world')
 print('This program was made by Rebecca')

biljett = 100  # biljettpris.
pengar = 200  # pengar på fickan.
summa = pengar - biljett
print("Det blir ", (summa), "kronor över.")
hälften = 200 - 100 / 2
print("Hälften är:", f"{hälften:.0f}", "kr.")  # Visar utan decimaler.

tal1 = int(input("Skriv ett heltal ")) # Första heltalet från användaren.
tal2 = int(input("Skriv ett till heltal ")) # Andra heltalet från användaren. 
summan = tal1 + tal2 # Adderar talen.
print(summan)

jacka = 2000 # Jackans pris.
rea = 1000 # Rean på jackan. 
betala = jacka - rea # Vad man ska betala.
print(betala,"kr.") 

pris = 2000 # Jackans pris.
rea_procent = 50 # Rean på jackan.
slut_pris = pris * rea_procent / 100 # Vad man ska betala.
print(slut_pris) 

jacka = 2000
procent = int(input("Skriv en procentsats"))
slutpris = jacka * procent / 100
print(f"{slutpris:.0f}")