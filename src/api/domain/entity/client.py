from dataclasses import dataclass


@dataclass
class Client:
    id: int
    username: str
    email: str