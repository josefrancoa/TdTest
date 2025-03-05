from unittest.mock import Mock
import pytest
from CartePizerria import CartePizzeria

def test_is_empty():
    cartePizzeria = Mock()
    assert cartePizzeria.is_empty() == True

