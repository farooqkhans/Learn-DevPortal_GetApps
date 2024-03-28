import time
from urllib.parse import urlparse
from oauthlib import oauth1
import uuid
from CloudSecret import CloudSecret
import configparser

# FILEPATH: /Users/fkhan/work/react-demo/code-contribution/DevPortal-OAuth1-GetApps/src/main/java/com/oauthImp/app/GetOAuthValue.py


class GetOAuthValue:
  def __init__(self):
    self.config = configparser.ConfigParser()
    self.config.read("config/config.ini")

  def get_auth_value(self):
    consumer_key = self.config.get("OAuth", "siteId")
    cs = CloudSecret()
    consumer_secret = cs.getSharedSecret()
    app_id = self.config.get("OAuth", "appId")
    client = oauth1.Client(consumer_key, client_secret=consumer_secret)
    uri = urlparse(self.config.get("OAuth", "devportalDomain") + "/api/v1/management/applications/" + app_id)

    timestamp = str(int(time.time()))
    random_id = str(uuid.uuid4())

    # Generate the OAuth parameters
    parameters = {
      "oauth_version": "1.0",
      "oauth_consumer_key": consumer_key,
      "oauth_signature_method": "HMAC-SHA1",
      "oauth_timestamp": timestamp,
      "oauth_nonce": random_id
    }

    # Construct the OAuth request
    body = None  # Assign a value to 'body' before using it
    headers = {}  # Assign a value to 'headers' before using it
    uri, headers, body = client.sign(uri.geturl(), http_method="GET", body=body, headers=headers)

    
    auth_value = headers["Authorization"]

    return auth_value

  # def main():
  #     vos = ValidateOAuthSignature()
  #     vos.get_auth_value()
