import requests

URL = "https://hooks.slack.com/services/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"
DATA = {"text": "Hello, World! This is Drone!"}


requests.post(url=URL, json=DATA)

print('test')
