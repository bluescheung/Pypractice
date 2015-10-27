#!usr/bin/env python3
from xml.parsers.expat import ParserCreate
class WeatherSaxHandler(object):
    def __init__(self):
        self._weathers = []
    def start_element(self,name,attrs):
        if name == 'yweather:location':
            self._city = attrs['city']
            self._country = attrs['country']
        elif name == 'yweather:condition':
            self._today = attrs['date'].split(',')[0]
            print(self._today)
        elif name == 'yweather:forecast':
            if len(self._weathers) == 0:
                if attrs['day'] == self._today:
                    self._weathers = []
            aweather = {}
            aweather['text'] = attrs['text']
            aweather['high'] = attrs['high']
            aweather['low'] = attrs['low']
            self._weathers.append(aweather)

def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml)
    return {
        'city':handler._city,
        'country':handler._country,
        'today':{
            'text':handler._weathers[0]['text'],
            'low':handler._weathers[0]['high'],
            'high':handler_weathers[0]['low']
        },
        'tomorrow':{
            'text':handler._weathers[1]['text'],
            'low':handler._weathers[1]['high'],
            'high':handler._weathers[1]['low']
        }
    }
