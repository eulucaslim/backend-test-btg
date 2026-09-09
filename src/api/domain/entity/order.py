from dataclasses import dataclass
from typing import List

from src.api.domain.entity.product import Product


@dataclass(frozen=True)
class Order:
    id: int
    client_id: int
    items: List[Product]
