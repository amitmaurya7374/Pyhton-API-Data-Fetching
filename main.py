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
# Sending a request to an api
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")  # get a data from url and return a response
# print(response.status_code)  # give statuscode
# print(response.json())  # give json data
# we can handle an exception using raise_for_status
response.raise_for_status()  # this hanlde our http exceptions
data = response.json()
print(data)
# getting specific data from json
iss_latitude = data["iss_position"]["latitude"]
iss_longitude = data["iss_position"]["longitude"]

print(iss_longitude)
print(iss_latitude)
