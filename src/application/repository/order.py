from abc import ABC, abstractmethod
from typing import List

from domain.entity.order import Order


class OrderRepository(ABC):

    @abstractmethod
    def save(self, *args) -> Order:
        ...

    @abstractmethod
    def get(self, id: int) -> Order:
        ...

    @abstractmethod
    def get_all(self) -> List[Order]:
        ...

    @abstractmethod
    def update(self, *args) -> Order:
        ...

    @abstractmethod
    def delete(self, id: int) -> None:
        ...
