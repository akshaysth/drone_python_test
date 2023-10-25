import requests

URL = "https://hooks.slack.com/services/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"
DATA = {"text": "Hello, World!"}
HEADERS = {
    "Content-Type": "application/json",
}


requests.post(url=URL, headers=HEADERS, data=DATA)

print('test')
