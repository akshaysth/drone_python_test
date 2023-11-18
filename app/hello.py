import requests


def hello():
    return "hello world!"


def get_ip():
    return requests.get("https://ifconfig.me").text


if __name__ == "__main__":
    hello()
