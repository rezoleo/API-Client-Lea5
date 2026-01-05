from .User import User


class Machine:
    def __init__(
        self, id, name, mac, created_at, updated_at, ip, url, internet_expiration
    ):
        self.id = id
        self.name = name
        self.mac = mac
        self.created_at = created_at
        self.updated_at = updated_at
        self.ip = ip
        self.url = url
        self.internet_expiration = internet_expiration

    def __repr__(self):
        return f"Machine({self.id}, {self.name}, {self.mac}, {self.created_at}, {self.updated_at}, {self.ip}, {self.url}, {self.internet_expiration})"
