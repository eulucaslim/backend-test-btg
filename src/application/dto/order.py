from dataclasses import dataclass
from application.dto.product import ProductDTO

@dataclass(frozen=True)
class OrderDTO:
    id: int
    client_id: int
    items: list[ProductDTO]