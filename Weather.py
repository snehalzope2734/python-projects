import requests
api_key = 'a455c7faa8b37e42b24a3f0f3c59bf01'
print("Hello \n its an weather project where you got the details about weather of any city \nSo Please Try!!!")
n = int(input("How many city's weather u want to know?"))
for i in range(n): 
   
   city = input('Enter city name: ')

   url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

   response = requests.get(url)

   if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f'Temperature: {temp} K')
        print(f'Description: {desc}')
   else:
        print('Error...................Retry After Some Time.')
    