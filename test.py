import requests

URL = "https://hooks.slack.com/services/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"
DATA = {"text": "Hello, World! This is Drone!"}


requests.post(url=URL, json=DATA)

print('test')
