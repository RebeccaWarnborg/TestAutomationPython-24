"""
CI/CD-Uppgift

1. Beskriv ett CI/CD-flöde för ett tänkt projekt (till exempel en Flask-app eller
webbtjänst). 

a. Vad händer när utvecklaren pushar kod?
- När utvecklaren pushar kod till GitHub:
- En CI-pipeline (t.ex. via GitHub Actions) triggas automatiskt.
- Pipen hämtar koden, installerar beroenden och kör fördefinierade jobb, såsom testning, linters, och eventuellt byggsteg.
- Om allt lyckas kan ett CD-steg ta vid och rulla ut ändringarna till staging/production. 

b. Vilka tester ska köras?
- Enhetstester (unit tests) - testa funktioner isolerat.
- Integrationstester - säkerställa att olika delar fungerar tillsammans, t.ex. DB-anrop.
- End-to-end-tester (med t.ex. Playwright eller Selenium) - om det är en webbtjänst. 
- Linter - kontrollera kodstil och potentiella fel. 
- Test coverage - säkerställa att tillräckligt stor del av koden testas.

c. När och hur byggs applikationen?
- Bygg sker oftast efter att testerna klarat sig.
- Flask-appar behöver inte "kompileras", men Docker-användning är vanligt. Då byggs en image:
  - docker build . -t mittrepo/minflaskapp
- Den pushas till Docker Hub/registry om testen passerat.

d. Rita flödet som en enkel bild eller lista.
    1. Utvecklaren pushar till main eller develop.
    2.CI startar:
      - Installerar beroenden
      - Kör linter + tester
    3. Om OK:
      - Bygger Docker-image
      - Pusha till registry
    4. CD startar:
      - Drar senaste image
      - Rullar ut till staging/production (t.ex. via Heroku, GCP eller en server)

e. Vad skulle kunna gå fel i flödet?
- Failing tester blockerar deployment.
- Saknade beroenden i byggsteget.
- Felaktiga secrets/environment-variabler.
- Deploy-script kraschar.
- Versioneringskonflikter (ex: fel branch deployas).

f. Vilka tester är viktigast i just ditt flöde?
- Enhetstester för kärnlogik.
- Integrationstester mot databas/API.
- E2E-tester om appen har UI.
- Linter för kodkvalitet.

g. Hur kan testning förbättra kvaliteten?
- Fångar buggar tidigt = mindre kostsamt.
- Säkrar att gammal funktionalitet fortfarande funkar (regressionstester).
- Minskar risken för att bruten kod når produktion.
- Gör teamet tryggare att refaktorera/ändra kod.

2. Hur tror du att automatiserad testning påverkar en utvecklares vardag?
- Minskar stress och osäkerhet - man vågar ändra kod utan att vara rädd.
- Snabb återkoppling på om något gick sönder.
- Ger struktur och disciplin i utvecklingsprocessen.
- Kan vara segt i början att sätta upp, men lönar sig snabbt.

3. Vad är en fördel och en nackdel med att ha testning inbyggd i CI/CD-flödet?
Fördel: Man upptäcker problem automatiskt och tidigt - innan det nått produktion.
Nackdel: Kan göra pipelines långsamma om testerna är många eller ineffektiva. 

4. Om du skulle införa CI/CD i ett skarpt projekt - vad skulle du börja med?
  1. CI:
    - Sätta upp GitHub Actions eller liknande.
    - Lägga in testkörning + kodstilskontroll (linter).
  2. CD:
    - Bygga en Docker-image.
    - Deploy till stagingmiljö först.

"""