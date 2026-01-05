import requests
from .User import User
from .Machine import Machine


class ApiLea5:
    def __init__(self, url, apikey):
        """
        Initialize Api authentication.
        Url should be the api endpoint of Lea5.
        """
        self.url = url
        self.apikey = apikey

    def fetchUserById(self, id):
        response = requests.get(
            self.url + f"users/{id}", headers={"Authorization": f"Bearer {self.apikey}"}
        ).json()
        user = self._dataToUser(response)
        return user

    def fetchAllUsers(self):
        """
        Fetch all users in Lea5.
        """
        response = requests.get(
            self.url + "users", headers={"Authorization": f"Bearer {self.apikey}"}
        ).json()
        users = []
        for user_data in response:
            user = self._dataToUser(user_data)
            users.append(user)
        return users

    def fetchUserByUsername(self, username):
        """
        Fetch a user in Lea5 using its username.
        """
        response = requests.get(
            self.url + "users/" + username,
            headers={"Authorization": f"Bearer {self.apikey}"},
        ).json()
        user = self._dataToUser(response)
        return user

    def fetchMachineById(self, id):
        """
        Fetch a machine in Lea5 using its id.
        """
        try:
            response = requests.get(
                self.url + f"machines/{id}",
                headers={"Authorization": f"Bearer {self.apikey}"},
            ).json()
            machine = self._dataToMachine(response)
        except Exception as e:
            print(f"Error fetching machine by ID {id}: {e}")
            return None
        return machine

    def fetchAllMachines(self, has_connection=None):
        """
        Fetch all machines in Lea5.
        """
        response = requests.get(
            self.url + "machines",
            params={"has_connection": has_connection},
            headers={"Authorization": f"Bearer {self.apikey}"},
        ).json()
        machines = []
        for machine_data in response:
            machine = self._dataToMachine(machine_data)
            machines.append(machine)
        return machines

    def fetchMachineByMac(self, mac):
        """
        Fetch a machine in Lea5 using its mac address.
        """
        try:
            response = requests.get(
                self.url + "machines/" + mac,
                headers={"Authorization": f"Bearer {self.apikey}"},
            ).json()
            machine = self._dataToMachine(response)
        except Exception as e:
            print(f"Error fetching machine by MAC {mac}: {e}")
            return None
        return machine

    def createMachine(self, user, mac):
        """
        Create a machine in Lea5.
        user should be an instance of User.
        mac should be the mac address of the machine.
        """
        data = {"user_id": user.id, "machine": {"mac": mac, "name": "Machine"}}
        response = requests.post(
            self.url + "machines",
            json=data,
            headers={"Authorization": f"Bearer {self.apikey}"},
        )
        return response

    def _dataToUser(self, data):
        """
        Convert a dictionary to a User instance.
        """
        user = User(
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
            ntlm_password=data["ntlm_password"] if "ntlm_password" in data else None,
        )
        return user

    def _dataToMachine(self, data):
        """
        Convert a dictionary to a Machine instance.
        """
        machine = Machine(
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
