from requests import request
import json
import httpx
import asyncio
import jwt


def send(url, headers, payload):
    return request("POST", url, data=json.dumps(payload), headers=headers)


async def send_async(url, headers, payload):
    async with httpx.AsyncClient() as client:
        return (await client.post(url, data=json.dumps(payload), headers=headers))


def attach_tag_to_user(base_url, user_id, api_token, payload):
    """ This function used to add tag to userId."""

    url = f"{base_url}/v1/users/tag/{user_id}"

    headers = {
        "api_token": api_token,  # token for the bot
        "Content-Type": "application/json",
    }

    return asyncio.run(send_async(url, headers, payload))


def set_tag_for_user(base_url, user_id, tag, displayName, values, active, api_token):
    """ This function used to add tag to userId."""

    url = f"{base_url}/v1/users/tag/{user_id}"

    headers = {
        "api_token": api_token,  # token for the bot
        "Content-Type": "application/json",
    }

    payload = {
        "tag": tag,
        "displayName": displayName,
        "values": values,
        "active": eval(active)
    }

    return asyncio.run(send_async(url, headers, payload))


def insert_content(base_url, user_id, api_token, payload):
    """Insert or update content for your bot"""

    url = f"{base_url}/v1/content"

    headers = {
        "api_token": api_token,  # token for the bot
        "Content-Type": "application/json",
    }

    return asyncio.run(send_async(url, headers, payload))


def get_user_profile(api_token, base_url, user_id):
    """Get basic profile of the user"""

    url = f'{base_url}/v1/users/{user_id}'

    headers = {
        "api_token": api_token,
        "Content-Type": "application/json",
    }

    return request("GET", url, headers=headers)


def content_search(api_token, base_url, query):
    """Search content on your bot"""

    url = f'{base_url}/v1/content/search?q={query}'

    headers = {
        "api_token": api_token,
        "Content-Type": "application/json",
    }

    return request("GET", url, headers=headers)


def content_search_via_slug(api_token, base_url, slug):
    """Search content on your bot"""

    url = f'{base_url}/v1/content/{slug}'

    headers = {
        "api_token": api_token,
        "Content-Type": "application/json",
    }

    return request("GET", url, headers=headers)


def send_announcement(base_url, api_token, payload):
    """Send subscribed announcement"""

    url = f"{base_url}/v1/messages/announce"

    headers = {
        "api_token": api_token,
        "Content-Type": "application/json",
    }

    return asyncio.run(send_async(url, headers, payload))


def get_user_tags(api_token, base_url, user_id):
    """Get all tags for a specific userId"""

    url = f'{base_url} + "/v1/users/tags/{user_id}'

    headers = {
        "api_token": api_token,
        "Content-Type": "application/json",
    }

    return request("GET", url, headers=headers)


def request_handler(request):
    api_token = request.headers["api_token"]
    user_id = request.headers["user_id"]

    raw = request.data.get("raw", "")

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


def send_message(api_token, base_url, payload):
    url = base_url + "/v1/messages/send"

    headers = {
        "api_token": api_token,
        "Content-Type": "application/json"
    }

    return request("POST", url, data=json.dumps(payload), headers=headers)
