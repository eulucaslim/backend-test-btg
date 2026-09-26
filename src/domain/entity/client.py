from dataclasses import dataclass


@dataclass
class Client:
    username: str
    email: str
    id: int | None = None