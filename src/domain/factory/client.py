from domain.entity.client import Client

from email_validator import validate_email

class ClientFactory:

    @staticmethod
    def create(username: str, email: str) -> Client | None:

        if username is None and email is None:
            raise Exception("The Args are None!")

        if not validate_email(email):
            raise Exception("Email invalid!")

        return Client(username, email)