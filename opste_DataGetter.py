import json
import requests
from transliterate import translit

class DataGetter:
    def __init__(self, url = None, data = None):
        self.url = url
        self.data = data

    def gather_data(self):
        response = requests.get(self.url)
        if(response.ok):
            self.data = json.loads(response.text)
        else:
            raise Exception("Failed to get data from the server.")

    def filter_data(self, filter_func):
        self.data = filter_func(self.data)

    def save_data(self, path):
        with open(path, 'w') as file:
            json.dump(self.data, file)
    
    def tranlisterate(self):
         self.data = translit(str(self.data), 'sr', reversed=True)


    def set_url(self, url):
        self.url = url

    """ Lokalna funcija koja otvara fajl sa zeljenim drzavama i periodima"""
    def open_parameter(self, parameter: str) -> list:
        with open('./parameters/' + parameter + '.json', 'r') as file:
            parameter_file = json.load(file)
        parameter_out = parameter_file[parameter]
        parameter_out.sort()
        return parameter_out

    """ Funkcija koja pravi URL za API poziv"""
    def make_url(self, indicator) -> str:
        url = 'https://www.imf.org/external/datamapper/api/v1/' + indicator
        regions: list = self.open_parameter('regions')
        periods: list = self.open_parameter('periods')
        for region in regions:
            url += '/' + region
        if len(periods) > 0:
            url += '?periods='
            for period in periods:
                url += str(period) + ','
            url = url[:-1]
        return url