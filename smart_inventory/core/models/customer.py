import re
from core.exceptions.invalid_email import InvalidEmailException


class Customer:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
        self.validate_email()

    def validate_email(self) -> None:
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, self.email):
            raise InvalidEmailException("Invalid email format.")