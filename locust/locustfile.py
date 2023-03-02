from locust import HttpUser, task
import json

class WebsiteUser(HttpUser):

    @task
    def get_token(self):
        self.client.post("http://localhost:8000/auth/realms/master/protocol/openid-connect/token", {"client_id": "admin-cli", "username": "admin", "password": "admin", "grant_type": "password"}, headers={"Connection": "close"})

    # @task
    # def get_users(self):
    #     self.client.adapters.DEFAULT_RETRIES = 5
    #     r = self.client.post("http://localhost:8080/auth/realms/master/protocol/openid-connect/token", data= {"client_id": "admin-cli", "username": "admin", "password": "admin", "grant_type": "password"}, headers={"Connection": "close"}).text
    #     print(r)
    #     h =  {"Authorization": "Bearer "+json.loads(r)["access_token"], "Connection": "close"}
    #     self.client.get("http://localhost:8080/auth/admin/realms/master/users", headers=h, verify=False)



