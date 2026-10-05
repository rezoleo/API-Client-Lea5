from dataclasses import dataclass


@dataclass
class Machine:
    id: str
    name: str
    mac: str
    created_at: str
    updated_at: str
    ip: str
    url: str
    internet_expiration: str

    @classmethod
    def from_api(cls, data):
        """
        Convert a dictionary to a Machine instance.
        """
        machine = cls(
            id=data["id"],
            name=data["name"],
            mac=data["mac"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            ip=data["ip"],
            url=data["url"],
            internet_expiration=data["internet_expiration"],
        )
        return machine