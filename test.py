import requests

URL = "https://hooks.slack.com/services/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"
DATA = {"text": "Hello, World!"}
HEADERS = {
    "Content-Type": "application/json",
}


requests.post(url=URL, headers=HEADERS, data=DATA)

print('test')
