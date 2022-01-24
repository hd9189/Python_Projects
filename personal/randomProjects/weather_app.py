import requests

API_KEY = "627a9b406a8d569fccf7a734bc12d9df"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
#create url off of base url to take specific information from website
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

#sending a request to website
response = requests.get(request_url)

#see the status of the response for request, see if the they have info on the city, the number represents the status
#successful response
if response.status_code == 200:
    #request json format
    data = response.json()
    weather = data['weather'][0]['description']
    print("Weather is: " + weather)
    temperature = round(data['main']['temp'] - 273.15, 2)
    print("Temperature is: ", temperature, "celcius")

else:
    print("An Error occurred.")