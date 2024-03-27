import main
from io import StringIO
import sys

def test_afficher_liste(mocker):
    mocker.patch('builtins.input', return_value="1,3,5,6")
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "['1', '3', '5', '6']"
    assert expected_value in output

def test_somme(mocker):
    mocker.patch('builtins.input', return_value="1,3,5,6")
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "15"
    assert expected_value in output

def test_moyenne(mocker):
    mocker.patch('builtins.input', return_value="1,3,5,6")
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "3.75"
    assert expected_value in output

def test_moyenne_sup(mocker):
    mocker.patch('builtins.input', return_value="1,3,5,6")
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "2"
    assert expected_value in output

def test_nombre_pair(mocker):
    mocker.patch('builtins.input', return_value="1,3,5,6")
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    expected_value = "1"
    assert expected_value in output