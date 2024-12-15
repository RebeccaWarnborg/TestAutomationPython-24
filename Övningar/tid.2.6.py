sekunder = int(input("Ange antal sekunder: "))
timmar = sekunder // 3600  # 1 timme = 3600 sekunder
sekunder_resterande = sekunder % 3600
minuter = sekunder_resterande // 60
sekunder_kvar = sekunder_resterande % 60
print(f"{sekunder} sekunder är lika med:")
print(f"{timmar} timmar, {minuter} minuter och {sekunder_kvar} sekunder.")

