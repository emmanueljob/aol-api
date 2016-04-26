import requests
import json
import urllib
from urllib import urlencode

class Connection:

    authorization_token = None

    def __init__(self, username=None, password=None, url=None):
        Connection.password = password
        Connection.username = username
        Connection.url = url

    def get_authorization(self):
        if Connection.authorization_token is None:
            Connection.authorization_token = self.authorize()

        return {'Authorization': Connection.authorization_token}

    def authorize(self):
        # auth_url = "https://elsuat-sso.corp.aol.com/opensso/UI/Login"
        auth_url = "https://elsuat-ext.corp.aol.com:443/opensso/identity/authenticate?uri=realm=aolext"

        username = Connection.username
        password = Connection.password

        credentials = {
            "username": username,
            "password": password
        }

        credentials['SunQueryParamsString'] = 'cmVhbG09YW9sZXh0'

        headers = {'Referer': 'https://dsp.accuenmedia.com'}

        response = requests.post(auth_url, headers=headers, data=credentials, allow_redirects=True, verify=False)

        if response is not None:
            Connection.authorization_token = "ELS {0}".format(response.cookies['iPlanetDirectoryProuat'])
        else:
            raise Exception('unable to authenticate')

        return Connection.authorization_token
