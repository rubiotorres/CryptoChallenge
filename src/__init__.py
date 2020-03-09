from connectDB import *
from jsoncontent import *
from crypto import *

if __name__ == "__main__":
    url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=26a1b1237334125b08bc92611fca866f706fe5eb"
    urlpost = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=26a1b1237334125b08bc92611fca866f706fe5eb"
    con = ConnectDB(url,urlpost)
    json = jsoncontent(con.getRequest())
    mssg = decipher(json.json)
    json.exportJson()
    print(json.json)
    json.json["decifrado"] = mssg.decipherText()
    json.sha1Response()
    print(json.json)
    json.exportJson()
    con.postresponse()


