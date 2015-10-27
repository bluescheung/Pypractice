#!usr/bin/env python3
from xml.parsers.expat import ParserCreate
class WeatherSaxHandler(object):
    def __init__(self):
        self.weather = dict()
    def start_element(self,name,attrs):
        if name == 'yweather:location':
            self.weather['city'] = attrs['city']
            self.weather['country'] = attrs['country']
        if name == 'yweather:forecast':
            if 'today' not in self.weather.keys():
                self.forecast('today',attrs)
            elif 'tomorrow' not in self.weather.keys():
                self.forecast('tomorrow',attrs)
    def forecast(self,date,attrs):
        self.weather[date]=dict()
        self.weather[date]['low'] = int(attrs['low'])
        self.weather[date]['high'] = int(attrs['high'])
        self.weather[date]['text'] = attrs['text']
def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml)
    return (handler.weather)

if __name__=='__main__':
    parse_weather(data)
