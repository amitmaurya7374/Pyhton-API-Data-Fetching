"""In this file we will learn about API(Application Interface Programming)"""

"""
What is Api?
Api is a set of functions,commands,protocols and objects.That a programmer use to create a software.
or interact with an external system.\n
How it Works?           
                        |----|
             requests   |    |
your Program =========> |API |=====> External system
            <========== |    | =====
             reponse    |----|
             
             
What Is Api Endpoints?
Api endpoints is actually a location where a data is stored.
"""
import datetime as dt

# Sending a request to an api
import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")  # get a data from url and return a response
# # print(response.status_code)  # give statuscode
# # print(response.json())  # give json data
# # we can handle an exception using raise_for_status
# response.raise_for_status()  # this hanlde our http exceptions
# data = response.json()
# print(data)
# # getting specific data from json
# iss_latitude = data["iss_position"]["latitude"]
# iss_longitude = data["iss_position"]["longitude"]
# iss_position = (iss_latitude,iss_longitude)
# print(iss_position)

"""Understanding API Parameters => actually means give a input to an api for getting a desired output.
some api take inputs for work properly
"""
parameters = {
    "lat": 28.4089,
    "lng": 77.3178,
    "formatted": 0
}
# response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={parameters['lat']}&lng={parameters['lng']}")
# Another way to pass parameters
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)  # this give unix time which is 12 hr
print(sunset)
current_datetime = dt.datetime.now()

print(current_datetime.hour)  # this give 24 hr format

# with open("sun_data.json","w") as file:
#     json.dump(data,file,indent=4)
