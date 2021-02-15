import requests


def get_storehouse_size():
    response = requests.get(f'http://127.0.0.1:5000/scheme')

    if response.status_code == 200:  # If request completed successfully
        res = response.json()
    else:
        res = None
    return res


if __name__ == "__main__":
    size = get_storehouse_size()
    print(size)
