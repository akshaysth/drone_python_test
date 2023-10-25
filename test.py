import requests

URL = "https://rocket.hyperios.space/hooks/65398b8e33c299ed89abc20c/chtNrvpjqx4vjQYL2KpcuTDr7RDHSu6W6SAJzdL9c7QAjwf8"
DATA = {"text": "Hello, World! This is Drone!"}


requests.post(url=URL, json=DATA)

print('test')
