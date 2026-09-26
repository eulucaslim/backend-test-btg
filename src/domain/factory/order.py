from dataclasses import dataclass
from typing import List

from domain.entity.order import Order
from domain.entity.product import Product


@dataclass(frozen=True)
class OrderFactory:

    @staticmethod
    def create(client_id: int, items: List[Product | None]) -> Order | None:

        if client_id is None:
            raise Exception("Client_id Not included!")

        return Order(client_id, items)
