import re

class Email:

    def __init__(self, email):
        self.email = self._is_valid_email(email)

    def _is_valid_email(self, email):
        regex = "^[a-z0-9]+[\_]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(regex, email):
            raise ValueError("It's not an email address.")
        return email
