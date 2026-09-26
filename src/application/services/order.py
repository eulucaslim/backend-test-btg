from application.dto.order import OrderDTO
from application.mappers.order import OrderMapper
from application.repository.order import OrderRepository
from domain.entity.order import Order

class OrderService:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create(self, dto: OrderDTO) -> Order | None:
        entity: Order | None = OrderMapper.to_entity(dto)
        self.repository.save(entity)
        return entity

    def get(self, id: int) -> Order | None:
        ...