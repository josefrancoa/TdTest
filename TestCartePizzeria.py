import pytest
from unittest.mock import  Mock
from CartePizzeria import CartePizzeria

def test_is_empty():
    cartePizzeria = CartePizzeria()
    assert cartePizzeria.is_empty() == True

def test_add_pizza():

    carte = CartePizzeria()

    mock_pizza = Mock()
    mock_pizza.name = "Margherita"

    carte.add_pizza(mock_pizza)

    assert carte.nb_pizzas() == 1
    assert mock_pizza in carte.pizzas

def test_remove_pizza():
    carte = CartePizzeria()
    mock_pizza = Mock()
    mock_pizza.name = "Bolognaise"
    carte.add_pizza(mock_pizza)
    carte.remove_pizza("Bolognaise")

    assert carte.nb_pizzas() == 0


