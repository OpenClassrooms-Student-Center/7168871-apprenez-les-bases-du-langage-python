from io import StringIO
import sys
from main import main
from operations import multiplication, addition


def test_main():
    output = StringIO()
    sys.stdout = output
    main()
    output_value = output.getvalue().strip()
    sys.stdout = sys.__stdout__
    assert (
        "15\n   32" in output_value
    ), "Les fonctions ne sont pas correctement appelées, ou vous n'affichez pas les résultats."
    
def test_multiplication():
  assert multiplication(10, 5) == 50, "La fonction multiplication n'est pas correctement définit"

def test_addition():
  assert addition(10, 5) == 15, "La fonction addition n'est pas correctement définie."
