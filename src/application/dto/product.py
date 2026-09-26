from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class ProductDTO:
    name: str
    quantity: int
    price: Decimal