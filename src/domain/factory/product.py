from dataclasses import dataclass
from decimal import Decimal

from domain.entity.product import Product

@dataclass(frozen=True)
class ProductFactory:

    @staticmethod
    def create(name: str, quantity: int, price: Decimal) -> Product | None:

        if quantity <= 0 or price <= 0.0:
            raise Exception("The value is less than zero.")

        return Product(name, quantity, price)