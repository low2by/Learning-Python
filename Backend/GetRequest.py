import requests
import hashlib
import json

url = "https://api.close.com/buildwithus/"

def main():

    try:
        response = requests.get(url)

        response.raise_for_status()

        print("Status Code:", response.status_code)
        print("Body:\n", response.text)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except Exception as err:
        print(f"Other error occurred: {err}")

    data = response.json()
    key = data["key"].encode("utf-8")
    traits = data["traits"]
    hashes = []
    for trait in traits:
        h = hashlib.blake2b(trait.encode('utf-8'), key=key, digest_size=64)
        hashes.append(h.hexdigest())

    post_response = requests.post(url, json=hashes)
    post_response.raise_for_status()

    print(post_response.text)

if __name__ == '__main__':
    main()