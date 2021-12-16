from typing import Optional

class User:
    name:str
    email: str
    secret_child: Optional[str]

    def __init__(self, name, email):
        self.name = name
        self.email = email
