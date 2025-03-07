import pytest
from unittest.mock import  Mock
from CartePizzeria import CartePizzeria
from Pizza import Pizza
from Boisson import Boisson
from Dessert import Dessert

def test_is_empty():
    cartePizzeria = CartePizzeria()
    assert cartePizzeria.is_empty() == True

    pizza = Mock(spec=Pizza)
    pizza.name = "Bolo"
    cartePizzeria.add(pizza)
    assert cartePizzeria.is_empty() == False

    cartePizzeria.remove("Bolo")
    assert cartePizzeria.is_empty() == True


def test_add_pizza():
    carte = CartePizzeria()

    mock_pizza = Mock(spec=Pizza)
    mock_pizza.name = "Margherita"

    carte.add(mock_pizza)

    assert carte.nb_pizzas() == 1
    assert mock_pizza in carte.pizzas



def test_remove():
    carte = CartePizzeria()
    mock_pizza = Mock(spec=Pizza)
    mock_pizza.name = "Bolognaise"
    carte.add(mock_pizza)
    carte.remove("Bolognaise")

    assert carte.nb_pizzas() == 0

    
def test_nb_pizza():
    carte = CartePizzeria()
    assert carte.nb_pizzas() == 0
    
    mock_pizza1 = Mock(spec=Pizza)
    mock_pizza1.name = "Margherita"
    carte.add(mock_pizza1)
    assert carte.nb_pizzas() == 1
    
    mock_pizza2 = Mock(spec=Pizza)
    mock_pizza2.name = "Peperoni"
    carte.add(mock_pizza2)
    assert carte.nb_pizzas() == 2


def test_nb_drinks():
    carte = CartePizzeria()
    assert carte.nb_drinks() == 0

    drink1 = Mock(spec=Boisson)
    drink1.name = "Coca"
    carte.add(drink1)
    assert carte.nb_drinks() == 1

    drink2 = Mock(spec=Boisson)
    drink2.name = "Ice Tea"
    carte.add(drink2)
    assert carte.nb_drinks() == 2


def test_nb_desserts():
    carte = CartePizzeria()
    mock_dessert1 = Mock(spec=Dessert)
    mock_dessert1.name = "Tiramisu"
    mock_dessert2 = Mock(spec=Dessert)
    mock_dessert2.name = "Flan"

    carte.add(mock_dessert1)
    carte.add(mock_dessert2)

    assert carte.nb_desserts() == 2
    assert mock_dessert1 in carte.desserts
    assert mock_dessert2 in carte.desserts

