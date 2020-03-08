
class decipher():

    def __init__(self,json):
      self.json = json
    
    def decipherText(self):
        jsonResponse = str("")

        for letter in self.json["cifrado"].lower():
          compontent = str(chr(ord(letter)+3)) 
          if(ord(letter)<=97):
            jsonResponse = jsonResponse + letter
          elif(ord(letter)+3>122):
            jsonResponse = jsonResponse + str(chr(96 + (122 - ord(letter))))
          else:
            jsonResponse = jsonResponse + str(chr(ord(letter)+self.json["numero_casas"]))
        return jsonResponse