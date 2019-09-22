import json
from typing import Dict, Optional
import requests


class PushoverException(Exception):
    pass


def load_creds() -> Dict:
    data = open("/etc/pushover-credentials.json").read()
    return json.loads(data)


def pushover(message: str,  # pylint: disable=R0913
             title: Optional[str] = None,
             priority: int = -1,
             api_token: Optional[str] = None,
             url: Optional[str] = None,
             url_title: Optional[str] = None,
             sound: Optional[str] = None,
             retry: int = 30,
             expire: int = 3600) -> None:
    '''
    Priority
    -2: No notification / Alert
    -1: Quiet notification
     1: High priority (Bypass quiet hours)
     2: Always require user confirmation
    '''
    creds = load_creds()
    if not api_token:
        api_token = creds["default-api-token"]
    user = creds["user"]
    payload = {
        "token": api_token,
        "user": user,
        "message": message,
        "priority": priority
    }
    if priority == 2:
        payload["expire"] = expire
        payload["retry"] = retry
    if title:
        payload["title"] = title
    if url:
        payload["url"] = url
    if url_title:
        payload["url_title"] = url_title
    if sound:
        payload["sound"] = sound
    response = requests.post("https://api.pushover.net/1/messages.json",
                             data=payload)
    if response.status_code != 200:
        raise PushoverException("Response Status Code: %s\n\tContent:%s" %
                                (response.status_code, response.content))
    content = json.loads(response.content)
    if content["status"] != 1:
        raise PushoverException("Response Status Code: %s\n\tContent:%s" %
                                (response.status_code, response.content))

SOUNDS = [
    "pushover",
    "bike",
    "bugle",
    "cashregister",
    "classical",
    "cosmic",
    "falling",
    "gamelan",
    "incoming",
    "intermission",
    "magic",
    "mechanical",
    "pianobar",
    "siren",
    "spacealarm",
    "tugboat",
    "alien",
    "climb",
    "persistent",
    "echo",
    "updown",
    "none",
]

if __name__ == "__main__":
    pushover("This is low priority test", "Test Title", priority=-1)
    pushover("This is a high priority test", priority=1)
    pushover("Confirmation Test", priority=2)
    pushover("Low priority test", priority=-2)
