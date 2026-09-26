from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Product:
    name: str
    quantity: int
    price: Decimal
    id: int | None = None
