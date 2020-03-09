import requests
import json


class ConnectDB():
    def __init__(self, url, urlpost):
        self.url = url
        self.urlpost = urlpost
        self.attempts = 0

    def getRequest(self):
        response = requests.get(self.url)
        if(response.status_code == 200):
            return response.json()
        else:
            self.attempts = self.attempts + 1
            self.getRequest()

    def postresponse(self):
        files = [
            ('answer', open(
                '/home/rubio/Documents/CryptoChallenge/data/exportedjson/answer.json', 'rb'))
        ]
        response = requests.post(self.urlpost, files=files)
        print(response.text.encode('utf8'))
