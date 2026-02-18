from __future__ import annotations

from typing import Dict

from .Pizza import Pizza
from .CartePizzeriaException import CartePizzeriaException


class CartePizzeria:
    def __init__(self) -> None:
        # On stocke par nom => accès/suppression rapide
        self._pizzas: Dict[str, Pizza] = {}

    def is_empty(self) -> bool:
        """Retourne un booléen indiquant si la carte est vide ou non."""
        return len(self._pizzas) == 0

    def nb_pizzas(self) -> int:
        """Retourne le nombre de pizzas de la carte."""
        return len(self._pizzas)

    def add_pizza(self, pizza: Pizza) -> None:
        """Ajoute une pizza à la carte."""
        self._pizzas[pizza.name] = pizza

    def remove_pizza(self, name: str) -> None:
        """
        Retire la pizza nommée de la carte.
        Si celle-ci n'existe pas, lève une exception CartePizzeriaException.
        """
        if name not in self._pizzas:
            raise CartePizzeriaException(f"Pizza '{name}' introuvable dans la carte.")
        del self._pizzas[name]
