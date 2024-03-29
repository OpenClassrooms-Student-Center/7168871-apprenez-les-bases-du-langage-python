import subprocess
import sys
import re

def run_main_file():
    python_cmd = "python" if sys.version_info.major == 2 else "python3"
    
    process = subprocess.Popen([python_cmd, "main.py"], stdout=subprocess.PIPE)
    output, error = process.communicate()

    return output.decode()


def test_title():
    output = run_main_file()
    exepected_output = "Exercice extraction HTML"
    assert exepected_output in output, "Le titre n'est pas correctement extrait"

def test_h1():
    output = run_main_file()
    exepected_output = "Bienvenue sur notre site web"
    assert exepected_output in output, "La balise h1 n'est pas correctement extraite"

def test_produit_10_euro():
    output = run_main_file()
    exepected_output = "10"
    assert exepected_output in output, "Le produit à 10 euros n'est pas correctement extrait"

def test_produit_20_euro():
    output = run_main_file()
    exepected_output = "20"
    assert exepected_output in output, "Le produit à 20 euros n'est pas correctement extrait"

def test_produit_30_euro():
    output = run_main_file()
    exepected_output = "30"
    assert exepected_output in output, "Le produit à 30 euros n'est pas correctement extrait"

def test_description_1():
    output = run_main_file()
    exepected_output = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    assert exepected_output in output, "La description 1 n'est pas correctement extraite"


def test_description_2():
    output = run_main_file()
    exepected_output = "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    assert exepected_output in output, "La description 2 n'est pas correctement extraite"


def test_description_3():
    output = run_main_file()
    exepected_output = "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    assert exepected_output in output, "La description 3 n'est pas correctement extraite"

def test_conversion_dollar():
    output = run_main_file()
    assert "24.0" in output, "Le produit 1 n'est pas correctement convertit"
    assert "36.0" in output, "Le produit 2 n'est pas correctement convertit"
    assert "12.0" in output, "Le produit 3 n'est pas correctement convertit"