#!/usr/bin/python

import json
import urllib2  # just incase you don't have this please pip install
import requests  # kindly use pip install to install requests i.e pip install requests

class checkWeather():

    def __init__(self, place):
        url = "http://api.apixu.com/v1/current.json"

        params = dict(
            key="b786dff6766747f49a7111928170803",
            q=place
        )

        resp = requests.get(url=url, params=params)
        self.resp = json.loads(resp.text)

    def check_humidity(self):
        return self.resp['current']['humidity']

    def check_temperature_in_celcius(self):
        return self.resp['current']['temp_c']

place = str(raw_input("Whats is the location that you want to check?"))

response = checkWeather(place)

print "The humidity for " + place + " is: " + str(response.check_humidity())