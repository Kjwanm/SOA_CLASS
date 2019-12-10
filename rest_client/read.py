import requests

if __name__ == "__main__":
    res = requests.get(
        url='http://localhost:8777/resource/t2'
    )
    print(res.status_code)
    print(res.json())

    res = requests.get(
        url='http://localhost:8777/resource_location/1'
    )
    print(res.status_code)
    print(res.json())