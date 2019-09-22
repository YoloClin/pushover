# Python-Pushover
I built this module some time ago and have a bunch of local repos which
rely on it. Also bin/wheres-my-phone is invaluable to my workflow.

I'd highly recommend you use an alternative module such as
![Thibauth/python-pushover](https://github.com/Thibauth/python-pushover)
Instead.

## Install
```bash
python setup.py install
echo '{
    "user": "your-pushover-user-token",
    "default-api-token": "your-api-token",
    "wheres-my-phone-token": "can-be-your-api-token-or-app-token"
}' > /etc/pushover-credentials.json
```

## Usage
```bash
pushover-notify "Message body" --title "Message Title" --priority 2
```

```python
pushovernotify.pushovernotify.pushover("Message body", "Title", -2)
# To use an app-specific token:
api_token = "your-pushover-app-token"
pushovernotify.pushovernotify.pushover("Message body", "Title", -2, api_token)
```

## TODO
Migrate to urllib to remove requestslib dependency
