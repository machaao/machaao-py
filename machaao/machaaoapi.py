from requests import request
import json
import httpx
import asyncio
import jwt


class Machaao:
    def __init__(self, api_token, base_url):
        self.api_token = api_token
        self.base_url = base_url

    def send_request(self, endpoint, payload):
        headers = {
            "api_token": self.api_token,  # token for the bot
            "Content-Type": "application/json",
        }
        url = self.base_url + endpoint

        return request("POST", url, data=json.dumps(payload), headers=headers)

    async def send_async_request(self, endpoint, payload):
        headers = {
            "api_token": self.api_token,  # token for the bot
            "Content-Type": "application/json",
        }
        url = self.base_url + endpoint

        async with httpx.AsyncClient() as client:
            return (await client.post(url, data=json.dumps(payload), headers=headers))

    def set_tag_to_user(self, payload, user_id):
        """ This function used to add tag to userId."""

        endpoint = f"/v1/users/tag/{user_id}"

        return asyncio.run(self.send_async_request(endpoint, payload))

    def insert_content(self, payload):
        """Insert or update content for your bot"""

        endpoint = "/v1/content"

        return asyncio.run(self.send_async_request(endpoint, payload))

    def get_user_profile(self, user_id):
        """Get basic profile of the user"""

        url = f'{self.base_url}/v1/users/{user_id}'

        headers = {
            "api_token": self.api_token,
            "Content-Type": "application/json",
        }

        return request("GET", url, headers=headers)

    def content_search(self, query):
        """Search content on your bot"""

        url = f'{self.base_url}/v1/content/search?q={query}'

        headers = {
            "api_token": self.api_token,
            "Content-Type": "application/json",
        }

        return request("GET", url, headers=headers)

    def content_search_via_slug(self, slug):
        """Search content on your bot"""

        url = f'{self.base_url}/v1/content/{slug}'

        headers = {
            "api_token": self.api_token,
            "Content-Type": "application/json",
        }

        return request("GET", url, headers=headers)

    def send_announcement(self, payload):
        """Send subscribed announcement"""

        endpoint = "/v1/messages/announce"

        return asyncio.run(self.send_async_request(endpoint, payload))

    def get_user_tags(self, user_id):
        """Get all tags for a specific userId"""

        url = f'{self.base_url}/v1/users/tags/{user_id}'

        headers = {
            "api_token": self.api_token,
            "Content-Type": "application/json",
        }

        return request("GET", url, headers=headers)

    def request_handler(self, request):
        api_token = request.headers["api_token"]
        user_id = request.headers["user_id"]

        raw = request.json.get("raw", "")

        if raw != "":
            input = jwt.decode(str(raw), api_token, algorithms=["HS512"])
            sub = input.get("sub", None)
            # print("Conditional")
            if sub and type(sub) is dict:
                sub = json.dumps(sub)

            if sub:
                decoded = json.loads(sub)
                messaging = decoded.get("messaging", None)

        return {
            "api_token": api_token,
            "user_id": user_id,
            "messaging": messaging
        }

    def extract_data(self, request):
        api_token = request.headers["api_token"]
        user_id = request.headers["user_id"]

        raw = request.json["raw"]

        if raw != "":
            input = jwt.decode(str(raw), api_token, algorithms=["HS512"])
            sub = input.get("sub", None)
            # print("Conditional")
            if sub and type(sub) is dict:
                sub = json.dumps(sub)

            if sub:
                decoded = json.loads(sub)
                messaging = decoded.get("messaging", None)

        return {
            "api_token": api_token,
            "user_id": user_id,
            "messaging": messaging
        }

    def send_message(self, payload):
        endpoint = "/v1/messages/send"

        return self.send_request(endpoint, payload)
