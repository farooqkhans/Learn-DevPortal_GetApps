# FILEPATH: /Users/fkhan/work/react-demo/code-contribution/DevPortal-OAuth1-GetApps/src/main/java/com/oauthImp/app/CloudSecret.py
import oauth2 as oauth
import httplib2
import json
import configparser

class CloudSecret:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config/config.ini")

    def getSharedSecret(self):
        # Define OAuth credentials
        clientKey = self.config.get("OAuth","clientKey")
        clientSecret = self.config.get("OAuth","clientSecret")
        siteId = self.config.get("OAuth","siteId")
        # Construct API endpoint URL
        url = self.config.get("OAuth","cloudDomain") + "/v1/internal/sites/" + siteId + "/sharedSecret"

        # Create OAuth consumer
        consumer = oauth.Consumer(clientKey, clientSecret)

        # Create HTTP client
        httpClient = httplib2.Http()

        # Sign the request with OAuth credentials
        request = oauth.Request.from_consumer_and_token(consumer, http_method='GET', http_url=url)
        request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, None)

        # Execute the request
        response, content = httpClient.request(url, 'GET', headers=request.to_header())

        # Parse the response string to a JSON object
        jsonResponse = json.loads(content)

        # Extract the value using the key. Replace "key" with the actual key.
        sharedSecret = jsonResponse["sharedSecret"]

        # Return the response as a string
        return sharedSecret
    