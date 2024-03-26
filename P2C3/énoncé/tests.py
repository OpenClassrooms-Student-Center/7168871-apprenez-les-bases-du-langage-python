from main import salaire_mensuel, salaire_hebdomadaire, salaire_horaire

def test_salaire_mensuel():
    input = 12000
    expected_output = 1000.0
    assert salaire_mensuel(input) == expected_output, "La fonction salaire_mensuel ne divise pas correctement le salaire annuel par 12."

def test_salaire_hebdomadaire():
    input = 4000
    expected_output = 1000
    assert salaire_hebdomadaire(input) == expected_output, "La fonction salaire_hebdomadaire ne divise pas correctement le salaire mensuel par 4."

def test_salaire_horaire():
    salaire_hebdomadaire = 1000
    horaire_hebdomadaire = 10
    expected_output = 100
    assert salaire_horaire(salaire_hebdomadaire, horaire_hebdomadaire) == expected_output, "La  fonction salaire_horaire ne divise pas correctement le salaire hebdomadaire par le nombre d'heure hebdomadaire."