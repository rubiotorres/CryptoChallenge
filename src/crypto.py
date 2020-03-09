
class decipher():

    def __init__(self,json):
      self.json = json
    
    def decipherText(self):
        jsonResponse = str("")

        for letter in self.json["cifrado"].lower():
          num = ord(letter)-self.json["numero_casas"]
          compontent = str(chr(num)) 
          if(ord(letter)<97):
            jsonResponse = jsonResponse + letter
          elif(num <97):
            jsonResponse = jsonResponse + str(chr(26 - num)))
          else:
            jsonResponse = jsonResponse + compontent
        return jsonResponse