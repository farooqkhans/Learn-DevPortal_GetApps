import json
from GetOAuthValue import GetOAuthValue
import urllib.request
import configparser

class GetApplication:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config/config.ini")
    def makeRequest(self):
        appId = self.config.get("OAuth","appId")
        url = self.config.get("OAuth","devportalDomain") + "/api/v1/management/applications/" + appId

        # Get the authorization value from ValidateOAuthSignature class
        getOAuthValue = GetOAuthValue()
        authorizationValue = getOAuthValue.get_auth_value()

        # Set the request headers
        headers = {
            "AUTHORIZATION": "" + authorizationValue
        }
        # Make the request
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        data = response.read().decode("utf-8")

        # Convert response to JSON and print
        jsonResponse = json.loads(data)
        print(json.dumps(jsonResponse, indent=4))

if __name__ == "__main__":
    getApp = GetApplication()
    getApp.makeRequest()
