import requests

city='Villa Park'
country='US'
api_key=''
api_url='http://api.aladhan.com/v1/timingsByCity'

params = {
    'city': city,
    'country': country
}

try:
    response = requests.get(api_url, params=params)
    print(response.status_code)
    #print(response.json())
    timings = response.json()['data']['timings']
    print(timings)
    #parse it

except requests.exceptions.RequestException as e:
        print(f"Error fetching prayer times: {e}")

