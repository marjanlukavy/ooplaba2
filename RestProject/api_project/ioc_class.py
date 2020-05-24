import requests
# http://127.0.0.1:8000/dog-api/?format=json
class APIConnection:
    def __init__(self, url):
        self.url = url

    def return_json(self):
        response = requests.get(self.url)
        data = response.json()
        return data

def das(data):
    return data.return_json()

class DogToJSON:

    def __init__(self, data):
        self.data = data

    def return_json_file(self):
        pass

class DogToCSV:

    def __init__(self, data):
        self.data = data

    def return_csv_file(self):
        pass

