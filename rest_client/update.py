import requests

if __name__ == "__main__":
    res = requests.put(
        url='http://localhost:8777/resource/t7',
        data={
            'temperature': 33.5,
            'datetime': '2019-10-01 08:18:00',
            'location': '1st Floor, 4th Engineering Building, KoreaTech'
        }
    )

    print(res.status_code)
    print(res.json())