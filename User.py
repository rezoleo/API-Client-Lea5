class User:
    def __init__(
        self,
        id,
        firstname,
        lastname,
        email,
        room,
        created_at,
        updated_at,
        url,
        username,
        internet_expiration,
        ntlm_password=None,
    ):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.room = room
        self.created_at = created_at
        self.updated_at = updated_at
        self.url = url
        self.ntlm_password = ntlm_password
        self.username = username
        self.internet_expiration = internet_expiration

    def __repr__(self):
        return f"User({self.id}, {self.firstname}, {self.lastname}, {self.email}, {self.room}, {self.created_at}, {self.updated_at}, {self.url}, {self.ntlm_password}, {self.username}, {self.internet_expiration})"
