from main import fruits

def test_kiwi_dans_liste():
    expected_value = "kiwi"
    assert expected_value in fruits, "kiwi n'est pas dans la liste"

def test_orange_supprime_liste():
    expected_value = "orange"
    assert expected_value not in fruits, "orange est toujours dans la liste"

def test_ananas_remplace_banane():
    replaced_value = "ananas"
    removed_value = "banane"
    assert replaced_value in fruits, "ananas n'a pas été ajouté dans la liste"
    assert removed_value not in fruits; "banane n'a pas été remplacé dans la liste"

def test_liste_trie():
    not_expected_value = ['pomme', 'ananas', 'kiwi']
    expected_value = ['ananas', 'kiwi', 'pomme']
    assert not_expected_value != fruits
    assert expected_value == fruits, "La liste n'est pas trié"