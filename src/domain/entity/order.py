from dataclasses import dataclass
from typing import List

from domain.entity.product import Product


@dataclass(frozen=True)
class Order:
    client_id: int
    items: List[Product | None]
    id: int | None = None
