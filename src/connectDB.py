import requests

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
        header = {"content-type": "application/json"}
        con = requests.post(self.urlpost, data=json, headers=header)
        print(con.status_code)