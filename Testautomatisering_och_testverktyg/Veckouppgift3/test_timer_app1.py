"""
Test Time App 

User stories:
[U1] Som en användare vill jag kunna skapa och ta bort widgets för funktionerna timer och anteckning,
så jag kan redigera efter önskemål och behov.

Acceptanskriterier:
[A1.1] När jag trycker på widget "Add Timer" ska en timer visas på skärmen.
[A1.2] När jag trycker på ikonen som simulerar en papperskord ska min timer försvinna.
[A2.1] När jag trycker på widget "Add Note" ska en tom ruta visas på skärmen som jag kan skriva text i.
[A2.2] När jag trycker på ikonen som simulerar en papperskord ska min note försvinna.


Testscenarier:
[T1]
1. Kontrollera att knappen "Add timer" finns på skärmen.
2. Tryck på knappen "Add timer".
3. Kontrollera att en timer visas på skärmen.
4. Tryck på knappen som simulerar en papperskorg och kontrollera att timer'n försvinner.

[T2]
1. Kontrollera att knappen "Add note" finns på skärmen.
2. Tryck på knappen "Add note". 
3. Kontrollera att en tom ruta för textinmatning visas på skärmen.
4. Tryck på knappen som simulerar en papperskorg och kontrollera att rutan anteckningen försvinner.

"""

from playwright.sync_api import sync_playwright, expect

def test_add_and_remove_timer():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Gå till webbsidan
        page.goto("https://lejonmanen.github.io/timer-vue/")

        # Kontrollera att "Add timer"-knappen finns
        add_timer_button = page.locator("text=Add timer")
        expect(add_timer_button).to_be_visible()

        # Klicka på "Add timer"-knappen
        add_timer_button.click()

        # kontrollera att en timer-widget dyker upp
        timer_widget = page.locator(".timer") 
        expect(timer_widget).to_be_visible()

        # Klicka på papperskorgsikonen för att ta bort timern
        delete_button = timer_widget.locator("div.icon.close") 
        delete_button.click()

        # Kontrollera att timern försvunnit
        expect(timer_widget).not_to_be_visible()

        browser.close()

def test_add_and_remove_note():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Gå till webbsidan
        page.goto("https://lejonmanen.github.io/timer-vue/")

        # Kontrollera att "Add note"-knappen finns
        add_note_button = page.locator("text=Add note")
        expect(add_note_button).to_be_visible()

        # Klicka på "Add note"-knappen
        add_note_button.click()

        # Kontrollera att en note-widget dyker upp
        note_widget = page.locator(".note") 
        expect(note_widget).to_be_visible()

        # Klicka på papperskorgsikonen för att ta bort anteckningen
        delete_button = note_widget.locator("div.icon.close")
        delete_button.click()

        # Kontrollera att anteckningen försvunnit
        expect(note_widget).not_to_be_visible()

        browser.close()