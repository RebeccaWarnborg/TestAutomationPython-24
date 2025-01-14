tottenham = int(input("Hur många mål gjorde Tottenham?:")) # ber användaren skriva in antal mål
liverpool = int(input("Hur många mål gjorde Liverpool?:")) # ber användaren skriva in antal mål

if liverpool == tottenham:     # om det blir lika
    print("Det blev oavgjort!") 
elif liverpool < tottenham:    # om Tottenham vinner och med antal mål
    skillnad = tottenham - liverpool
    print(f"Tottenham vann med {skillnad} mål.") 
elif liverpool > tottenham:    # om Liverpool vinner och med antal mål
    skillnad = liverpool - tottenham
    print(f"Liverpool vann med {skillnad} mål.")
