__author__ = 'gokhan'
import json, urllib2

JSON_URL = 'http://api.openweathermap.org/data/2.5/weather?lat=35&lon=139'


class jsonService(object):
    def getCurrentWeather(url):
        response = urllib2.urlopen(url)
        jsonData = json.loads(response)
        return jsonData

    def getCurrentWeatherByName(self, url, name):
        response = urllib2.urlopen(url, name)
        jsonData = json.load(response)
        return jsonData

    def writeJsonResponse(self):
        print jsonService().getCurrentWeather(JSON_URL)
