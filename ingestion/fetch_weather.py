import requests

URL='https://archive-api.open-meteo.com/v1/archive?latitude=28.46&longitude=77.03&start_date=2026-09-20&end_date=2026-10-20&hourly=temperature_2m,wind_speed_10m,rain'
response=requests.get(URL)
data=response.json()
len_hour_data=len(data["hourly"]["time"])
print("Hourly Time Length:", len_hour_data)
five_temps=data["hourly"]["temperature_2m"][:5]
print(five_temps)

