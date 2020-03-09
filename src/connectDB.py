import requests
import json

class ConnectDB():
    def __init__(self, url,urlpost):
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
    def postresponse(self,json):
        url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=26a1b1237334125b08bc92611fca866f706fe5eb"

        payload = {}
        files = [
            ('answer', open('/home/rubio/Documents/CryptoChallenge/exportedjson/answer.json','rb'))
        ]
        headers = {
            'Content-Type': 'multipart/form-data; boundary=--------------------------486920556469742056617375'
        }

        response = requests.post(url, files= files)

        print(response.text.encode('utf8'))