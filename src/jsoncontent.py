import json
import hashlib

class jsoncontent():
    def __init__(self, json):
        self.json = json
        
    def exportJson(self):
        with open('/home/rubio/Documents/CryptoChallenge/data/exportedjson/answer.json', 'w') as f:
            json.dump(self.json, f)
    
    @property
    def json(self):
        return self._json
    
    @json.setter
    def json(self,json):
        if(json == ""):
            raise ValueError("Erro: não é possível um livro sem titulo")
        self._json = json

    def sha1Response(self):
        self.json["resumo_criptografico"] = hashlib.sha1(self.json["decifrado"].encode('utf-8')).hexdigest()
