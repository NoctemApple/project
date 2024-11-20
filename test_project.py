import pytest
from project import translate_morse_to_text, apply_backspace, is_valid_morse

def test_translate_morse_to_text():
    # Test valid Morse code translation
    assert translate_morse_to_text(".- -... -.-.") == "ABC"
    assert translate_morse_to_text(".... . .-.. .-.. ---") == "HELLO"
    assert translate_morse_to_text(".. / .-.. --- ...- . / .--. -.-- - .... --- -.") == "I LOVE PYTHON"
    assert translate_morse_to_text(".---- ..--- ...--") == "123"

    # Test invalid Morse code
    assert translate_morse_to_text("...---...---") == "?"  # Invalid code returns "?"

    # Test empty string
    assert translate_morse_to_text("") == ""

def test_apply_backspace():
    # Test removing last character
    assert apply_backspace("HELLO") == "HELL"
    assert apply_backspace("H") == ""

    # Test empty string
    assert apply_backspace("") == ""

def test_is_valid_morse():
    # Test valid Morse code
    assert is_valid_morse(".- -... -.-.") is True
    assert is_valid_morse(".... . .-.. .-.. ---") is True
    assert is_valid_morse(".. / .-.. --- ...- . / .--. -.-- - .... --- -.") is True

    # Test invalid Morse code
    assert is_valid_morse("ABC") is False  # Contains invalid characters
    assert is_valid_morse("..# / ..") is False  # Contains invalid character "#"

    # Test empty string
    assert is_valid_morse("") is True

if __name__ == "__main__":
    pytest.main()
