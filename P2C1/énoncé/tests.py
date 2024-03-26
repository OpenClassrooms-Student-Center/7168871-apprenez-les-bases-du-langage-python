import main
from io import StringIO
import sys

def test_symbole_correct(mocker):
    mocker.patch('builtins.input', side_effect=['40', '10', '&'])
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'."
    assert expected_value in output

def test_addition(mocker):
    mocker.patch('builtins.input', side_effect=['5', '3', '+'])
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "8"
    assert expected_value in output

def test_soustraction(mocker):
    mocker.patch('builtins.input', side_effect=['10', '5', '-'])
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "5"
    assert expected_value in output

def test_multiplication(mocker):
    mocker.patch('builtins.input', side_effect=['4', '7', '*'])
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "28"
    assert expected_value in output

def test_division(mocker):
    mocker.patch('builtins.input', side_effect=['40', '10', '/'])
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "4"
    assert expected_value in output

def test_division_zero(mocker):
    mocker.patch('builtins.input', side_effect=['40', '0', '/'])
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "Erreur: impossible de diviser par zéro."
    assert expected_value in output