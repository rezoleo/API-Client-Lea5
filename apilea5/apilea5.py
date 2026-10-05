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
        self._url = url
        self._apikey = apikey
        self._session = requests.Session()
        self._session.headers.update({"Authorization": f"Bearer {self._apikey}"})

    def fetch_all_users(self):
        """
        Fetch all users in Lea5.
        """
        endpoint = self._url + "users"
        response = self._session.get(endpoint)
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
        endpoint = self._url + f"users/{username}"
        response = self._session.get(endpoint)
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
        endpoint = self._url + f"machines/{id}"
        response = self._session.get(endpoint)
        status = response.status_code
        if status != 200:
            raise ApiError(status, response.text)
        response = response.json()
        machine = Machine.from_api(response)
        return machine

    def fetch_all_machines(self, with_internet_access=False):
        """
        Fetch all machines in Lea5.
        """
        endpoint = self._url + "machines"
        params = {}
        if with_internet_access:
            params["with_internet_access"] = 1
        response = self._session.get(endpoint,params=params)
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
        endpoint = self._url + f"machines/{mac}"
        response = self._session.get(endpoint)
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
        endpoint = self._url + "machines"
        data = {"user_id": user.id, "machine": {"mac": mac, "name": "Machine"}}
        response = self._session.post(endpoint,json=data)
        status = response.status_code
        if status != 201:
            raise ApiError(status, response.text)
        return response

