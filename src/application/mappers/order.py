from application.dto.order import OrderDTO
from domain.entity.order import  Order
from domain.factory.order import OrderFactory
from domain.factory.product import ProductFactory


class OrderMapper:

    @staticmethod
    def to_entity(dto: OrderDTO) -> Order | None:
        products = [
            ProductFactory.create(p.name, p.quantity, p.price) for p in dto.items
        ]
        return OrderFactory.create(dto.client_id, products)