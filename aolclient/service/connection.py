import requests
import json
import urllib


class Connection:

    authorization_token = None

    def __init__(self, username=None, password=None, url=None):
        Connection.password = password
        Connection.username = username
        Connection.url = url

    def connect(self):
        headers = []
        headers.push(Connection.get_authorization())

    def get_authorization(self):
        if Connection.authorization_token is None:
            Connection.authorization_token = self.authorize()

        return {'Authorization': Connection.authorization_token}

    def authorize(self):
        auth_url = "https://elsuat-sso.corp.aol.com/opensso/UI/Login"
        credentials = {
            "IDToken1": Connection.username,
            "IDToken2": Connection.password
        }

        credentials['SunQueryParamsString'] = 'cmVhbG09YW9sZXh0'

        headers = {'Content-Type': 'application/json'}
        response = requests.post(auth_url, headers=headers, params=credentials, allow_redirects=False, verify=False)

        if response is not None and response.headers.get('x-AuthErrorCode', -1) == '0':
            Connection.authorization_token = "ELS {0}".format(response.cookies['iPlanetDirectoryProuat'])
        else:
            raise Exception('unable to authenticate')

        return Connection.authorization_token
