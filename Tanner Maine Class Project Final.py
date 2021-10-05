#Tanner Maine Class project (Week 7 Draft) 9/26/21

import requests
#initializes the requests library to gather data from the openweathermap web site.

welcome = input("Welcome to Tanner's Weather Program: Press Enter to Continue")

# requests weather data if user selects city.
def choose_city():
    city = input('Please Enter Your City Name: ')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=3cfb3ef209130bbc71e87da6c0f41baf&units=imperial'.format(city)
    res = requests.get(url)
    data = res.json()
    #stores data into a JSON file
    dataoutput(data)
    #calls the show_data function to display the forecast
#uses the requests library to request data from the openweathermap website.
    question = input('Do you want to do another search ? Type Yes or No: ')
    if question == 'Yes':
        main()
    if question == 'No':
        print("Thank you for using the program. Good Bye!")
        exit()
# Validates the program to loop until user tells it to stop.


# requesting the weather data is user selects zip code.
def choose_zip():
    zip_code = int(input('Please Enter Your Zip code: '))
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=7b706324b4eabcd51c89e9a27965806a'.format(zip_code)
    res = requests.get(url)
    data = res.json()
    dataoutput(data)
#uses the requests library to request data from the openweathermap website.
    loopquestion = input('Do you want to do another search ? Type Yes or No: ')
    if loopquestion == 'Yes':
        main()
    if loopquestion == 'No':
        print("Thank you for using the program. Good Bye!")
        exit()
# Validates the program to loop until user tells it to stop.


# Displays weather data from the requests library.
def dataoutput(data):
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    description = data['weather'][0]['description']
    humid = data['main']['humidity']
    wind_speed = data['wind']['speed']
    press = data['main']['pressure']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']

#All data derived from the API output web page 
# (See API Key Data Reference for example)

    print('Current Temperature : {} degrees fahrenheit'.format(temp))
    print('High Temperature : {} degrees fahrenheit'.format(hightemp))
    print('Low Temperature : {} degrees fahrenheit'.format(lowtemp))
    print('Description : {}'.format(description))
    print('Humidity : {} %'.format(humid))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Pressure : {} hPa'.format(press))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    
#I opted to add latitude and longitude in the forecast as an extra layer
# of validation to make sure the program is workign correctly.

# defining main function with while loop code to run the program


def main():
    while True:
        #Validates based on city name
        answer = input("Want to know the weather? Please type zip for zip code or city for city name: ")
        if answer == 'city':
            try:
                print("Alright, Connection established.")
                choose_city()
            #While researchign try blocks I tried to do somethign new here with the Exception function. 
            #The exception class essentially classifies an exception as anything that was not the answer the
            # program is expecting and retuns it as an error
            except Exception:
                print("hmm, You did not enter a valid name. Try again")
                choose_city()
        
        #Validates based on zip code
        if answer == 'zip':
            try:
                print("Alright, Connection established.")
                choose_zip()

            except Exception:
                print("hmm, You did not enter a valid zip code number. Try again")
                choose_zip()

        else:
            print("well, that is not one of the options. Try again.")


main() #Calls the main function