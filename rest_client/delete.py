import requests

if __name__ == "__main__":
    res = requests.delete(
        url='http://localhost:8777/resource/t7'
    )

    print(res.status_code)