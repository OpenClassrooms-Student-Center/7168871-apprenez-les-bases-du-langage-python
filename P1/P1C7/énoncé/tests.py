from main import fruits, couleur_banane

def test_fruits_dictionnaire():
  assert isinstance(fruits, dict), "fruits n'est pas un dictionnaire"

def test_banane_supprime():
    element_to_check = "banane"
    assert element_to_check not in fruits, "La clé banane n'a pas été correctement supprimée."

def test_pomme_valeur():
    expected_value = "vert"
    assert fruits["pomme"] == expected_value, "La clé pomme n'a pas été correctement modifiée avec la valeur vert"

def test_kiwi_dans_dictionnaire():
    element_to_check = "kiwi"
    expected_value = "vert"
    assert element_to_check in fruits, "la clé kiwi n'est pas dans le dictionnaire"
    assert fruits[element_to_check] == expected_value, "la clé kiwi n'a pas la bonne valeur : vert"

def test_contenu_final_dictionnaire():
    assert "pomme" in fruits
    assert "kiwi" in fruits
    assert "orange" in fruits
    assert fruits["pomme"] == "vert"
    assert fruits["kiwi"] == "vert"
    assert fruits["orange"] == "orange"

def test_extraire_couleur_banane():
    expected_value = "jaune"
    assert couleur_banane == expected_value, "La couleur de banane n'a pas été extraite : jaune"