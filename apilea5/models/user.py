from dataclasses import dataclass


@dataclass
class User:
    id: str
    firstname: str
    lastname: str
    email: str
    room: str
    created_at: str
    updated_at: str
    url: str
    username: str
    internet_expiration: str
    ntlm_password: str = None

    @classmethod
    def from_api(cls, data):
        """
        Convert a dictionary to a User instance.
        """
        user = cls(
            id=data["id"],
            firstname=data["firstname"],
            lastname=data["lastname"],
            email=data["email"],
            room=data["room"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            url=data["url"],
            username=data["username"],
            internet_expiration=data["internet_expiration"],
            ntlm_password=data.get("ntlm_password", None),
        )
        return user