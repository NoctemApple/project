import pytest
from project import translator, handle_backspace, clear_all

def test_translator():

    assert translator(".- -... -.-.") == "ABC"
    assert translator("... --- ...") == "SOS"
    assert translator(".../---/...") == "S O S"
    assert translator(".. / .-.. --- ...- . / .--. -.-- - .... --- -.") == "I LOVE PYTHON"
    assert translator("") == ""
    assert translator("...---...") == "?" # Test invalid Morse code

def test_handle_backspace():
    
    assert handle_backspace("...") == ".."
    assert handle_backspace("... --- .../") == "... --- ..."
    assert handle_backspace("") == ""

def test_clear_all():
    
    assert clear_all("... --- ...") == ""
    assert clear_all("... --- ...", "SOS") == ("", "")
    assert clear_all("", "") == ("", "")

if __name__ == "__main__":
    pytest.main()
