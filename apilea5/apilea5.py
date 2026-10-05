import requests

from .exceptions import ApiError
from .models import Machine, User


class ApiLea5:
    def __init__(self, url, apikey):
        """
        Initialize Api authentication.
        Url should be the api endpoint of Lea5.
        """
        if not url.endswith("/"):
            url += "/"
        self.url = url
        self.apikey = apikey

    def fetch_all_users(self):
        """
        Fetch all users in Lea5.
        """
        endpoint = self.url + "users"
        response = requests.get(
            endpoint,
            headers={"Authorization": f"Bearer {self.apikey}"}
        )
        status_code = response.status_code
        if status_code != 200:
            raise ApiError(status_code, response.text)
        response = response.json()
        users = []
        for user_data in response:
            user = User.from_api(user_data)
            users.append(user)
        return users

    def fetch_user_by_username(self, username):
        """
        Fetch a user in Lea5 using its username.
        """
        endpoint = self.url + f"users/{username}"
        response = requests.get(
            endpoint,
            headers={"Authorization": f"Bearer {self.apikey}"},
        )
        status = response.status_code
        if status != 200:
            raise ApiError(status, response.text)
        response = response.json()
        user = User.from_api(response)
        return user

    def fetch_machine_by_id(self, id):
        """
        Fetch a machine in Lea5 using its id.
        """
        endpoint = self.url + f"machines/{id}"
        response = requests.get(
            endpoint,
            headers={"Authorization": f"Bearer {self.apikey}"},
        )
        status = response.status_code
        if status != 200:
            raise ApiError(status, response.text)
        response = response.json()
        machine = Machine.from_api(response)
        return machine

    def fetch_all_machines(self, with_internet_access=None):
        """
        Fetch all machines in Lea5.
        """
        endpoint = self.url + "machines"
        params = {}
        if with_internet_access:
            params["with_internet_access"] = 1
        response = requests.get(
            endpoint,
            params=params,
            headers={"Authorization": f"Bearer {self.apikey}"},
        )
        status = response.status_code
        if status != 200:
            raise ApiError(status, response.text)
        response = response.json()
        machines = []
        for machine_data in response:
            machine = Machine.from_api(machine_data)
            machines.append(machine)
        return machines

    def fetch_machine_by_mac(self, mac):
        """
        Fetch a machine in Lea5 using its mac address.
        """
        endpoint = self.url + f"machines/{mac}"
        response = requests.get(
            endpoint,
            headers={"Authorization": f"Bearer {self.apikey}"},
        )
        status = response.status_code
        if status != 200:
            raise ApiError(status, response.text)
        response = response.json()
        machine = Machine.from_api(response)
        return machine

    def create_machine(self, user, mac):
        """
        Create a machine in Lea5.
        user should be an instance of User.
        mac should be the mac address of the machine.
        """
        endpoint = self.url + "machines"
        data = {"user_id": user.id, "machine": {"mac": mac, "name": "Machine"}}
        response = requests.post(
            endpoint,
            json=data,
            headers={"Authorization": f"Bearer {self.apikey}"},
        )
        status = response.status_code
        if status != 201:
            raise ApiError(status, response.text)
        return response

