from main import main
import os
import csv

def test_output():
    main()
    filename = "output.csv"
    assert os.path.exists(filename)
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for data in reader:
            match data["nom"]:
                case "Pierre Durand":
                    assert data["salaire"] == '540'
                case "Paul Dupont":
                    assert data["salaire"] == '615'
                case "Edouard Gentil":
                    assert data["salaire"] == '600'
                case _:
                    assert False
    os.remove(filename)