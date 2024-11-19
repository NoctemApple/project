import pytest
from project import translator


def test_letters():
    assert translator("... --- ...") == "SOS"
