from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Product:
    id: int
    name: str
    quantity: int
    price: Decimal
