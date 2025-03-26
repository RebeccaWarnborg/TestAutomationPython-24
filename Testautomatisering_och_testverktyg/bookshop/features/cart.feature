Feature: Hantera varukorg i webbutiken

  Scenario: Lägg till en bok i varukorgen
    Given en tom varukorg
    When jag lägger till boken "Testautomation" som kostar 259kr
    Then ska varukorgen innehålla 1 bok
    And totalsumman ska vara 259kr

  Scenario: Lägg till samma bok två gånger
    Given en tom varukorg
    When jag lägger till boken "Testautomation" två gånger
    Then ska varukorgen visa att boken har antal 2
    And totalsumman ska vara 518kr

  Scenario: Ta bort en bok från varukorgen
    Given en varukorg med boken "Testautomation"
    When jag tar bort boken "Testautomation"
    Then ska varukorgen vara tom

  Scenario: Tömma varukorgen helt
    Given en varukorg med flera böcker
    When jag tömmer varukorgen
    Then ska varukorgen vara tom
    And totalsumman ska vara 0kr