import requests

URL = "https://hooks.slack.com/services/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"
DATA = {"text": "Hello, World! This is Drone!"}


requests.post(url=URL, json=DATA)

print('test')
