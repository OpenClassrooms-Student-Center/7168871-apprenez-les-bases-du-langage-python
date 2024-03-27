import subprocess
import sys
import re

def run_main_file():
    python_cmd = "python" if sys.version_info.major == 2 else "python3"
    
    process = subprocess.Popen([python_cmd, "main.py"], stdout=subprocess.PIPE)
    output, error = process.communicate()

    return output.decode()


def test_affichage_nom():
    output = run_main_file()
    regex_pattern = r"[nN]om\s?:\s?[A-Za-z]+"
    match = re.search(regex_pattern, output)
    assert match is not None, "Le motif 'Nom: [Nom en lettres]' n'a pas été trouvé dans la console output."

def test_affichage_age():
    output = run_main_file()
    regex_pattern = r"[aA]ge\s?:\s?\d+"
    match = re.search(regex_pattern, output)
    assert match is not None, "Le motif 'Age: [Age en chiffres]' n'a pas été trouvé dans la console output."

def test_affichage_taille():
    output = run_main_file()
    regex_pattern = r"[tT]aille\s?:\s?\d+\.\d+"
    match = re.search(regex_pattern, output)
    assert match is not None, "Le motif 'Taille: [Taille en nombre flottant]' n'a pas été trouvé dans la console output."

def test_affichage_est_etudiant():
    output = run_main_file()
    regex_pattern = r"[Ee]st\s?étudiant\s?:\s?(True|False)"
    match = re.search(regex_pattern, output)
    assert match is not None, "Le motif 'Est étudiant: [Est etudiant en booléen]' n'a pas été trouvé dans la console output."

def test_affichage_type_nom():
    output = run_main_file()
    regex_pattern = r"[tT]ype\s?[nN]om\s?:\s?<class 'str'>"
    match = re.search(regex_pattern, output)
    assert match is not None, "Le motif 'Type nom: [Type nom]' n'a pas été trouvé dans la console output."

def test_affichage_type_age():
    output = run_main_file()
    regex_pattern = r"[tT]ype\s?[aA]ge\s?:\s?<class 'int'>"
    match = re.search(regex_pattern, output)
    assert match is not None, "Le motif 'Type age: [Type age]' n'a pas été trouvé dans la console output."

def test_affichage_type_taille():
    output = run_main_file()
    regex_pattern = r"[tT]ype\s?[tT]aille\s?:\s?<class 'float'>"
    match = re.search(regex_pattern, output)
    assert match is not None, "Le motif 'Type taille: [Type taille]' n'a pas été trouvé dans la console output."

def test_affichage_type_est_etudiant():
    output = run_main_file()
    regex_pattern = r"[tT]ype\s?[eE]st\s?[eEéÉ]tudiant\s?:\s?<class 'bool'>"
    match = re.search(regex_pattern, output)
    assert match is not None, "Le motif 'Type est étudiant: [Type est étudiant]' n'a pas été trouvé dans la console output."

