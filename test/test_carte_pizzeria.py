import pytest
from unittest.mock import Mock

from pizzeria.CartePizzeria import CartePizzeria
from pizzeria.CartePizzeriaException import CartePizzeriaException
from pizzeria.Pizza import Pizza


def test_is_empty_true_when_new() -> None:
    carte = CartePizzeria()
    assert carte.is_empty() is True


def test_nb_pizzas_zero_when_new() -> None:
    carte = CartePizzeria()
    assert carte.nb_pizzas() == 0


def test_add_pizza_with_mock_makes_card_not_empty() -> None:
    carte = CartePizzeria()

    pizza_mock = Mock(spec=Pizza)
    pizza_mock.name = "Margherita"

    carte.add_pizza(pizza_mock)

    assert carte.is_empty() is False
    assert carte.nb_pizzas() == 1


def test_add_two_pizzas_with_mocks_counts_2() -> None:
    carte = CartePizzeria()

    p1 = Mock(spec=Pizza)
    p1.name = "Margherita"

    p2 = Mock(spec=Pizza)
    p2.name = "Reine"

    carte.add_pizza(p1)
    carte.add_pizza(p2)

    assert carte.nb_pizzas() == 2


def test_remove_pizza_existing_removes_it() -> None:
    carte = CartePizzeria()

    pizza_mock = Mock(spec=Pizza)
    pizza_mock.name = "Reine"
    carte.add_pizza(pizza_mock)

    carte.remove_pizza("Reine")

    assert carte.nb_pizzas() == 0
    assert carte.is_empty() is True


def test_remove_pizza_unknown_raises_exception() -> None:
    carte = CartePizzeria()

    with pytest.raises(CartePizzeriaException):
        carte.remove_pizza("Inconnue")
