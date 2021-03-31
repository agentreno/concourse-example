import requests


def fetch_ip():
    resp = requests.get("http://icanhazip.com")

    return resp.text


if __name__ == "__main__":
    print(fetch_ip())
