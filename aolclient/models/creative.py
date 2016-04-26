import json

from aolclient.models.base import Base

from aolclient.service.connection import Connection


# campaign_ids = [77508, 77509, 77510, 77511, 77512, 77513]

class Creative(Base):

    obj_name = "creatives"

    def get_create_url(self):
        return '{0}/video-management/v1/organizations/{1}/creatives'.format(Base.connection.url, self.get('organization_id'))

    def get_creatives_by_campaign(self, organization_id, campaign_id):

        url = '{0}/video-management/v1/organizations/{1}/campaigns/{2}/creatives'.format(Base.connection.url, organization_id, campaign_id)

        method = 'GET'

        response = self._execute(method, url, '')

        return self._get_response_objects(response)

    def get_creatives_by_advertiser(self, organization_id, advertiser_id):

        url = '{0}/video-management/v1/organizations/{1}/advertisers/{2}/creatives'.format(Base.connection.url, organization_id, advertiser_id)

        method = 'GET'

        response = self._execute(method, url, '')

        return self._get_third_party_creative_response_objects(response)

    # add for THIRD PARTY VIDEO CREATIVES
    def _get_third_party_creative_response_objects(self, response):
        rval = []
        if response.status_code == 200:
            json_response = json.loads(response.text)
        else:
            print response.text
            raise Exception("Bad response code {0}".format(response.text))

        obj_list = []

        if 'data' in json_response and 'thirdPartyVideoCreatives' in json_response['data']:
            obj_list = json_response['data']['thirdPartyVideoCreatives']

        for obj in obj_list:
            new_obj = self.__class__(Base.connection)
            new_obj.import_props(obj)
            rval.append(new_obj)

        return rval

    def create_creatives_by_advertiser(self, organization_id, advertiser_id):
        url = '{0}/video-management/v1/organizations/{1}/advertisers/{2}/creatives'.format(Base.connection.url, organization_id, advertiser_id)

        method = 'POST'

        response = self._execute(method, url, json.dumps(self.export_props()))

        obj = self._get_response_object(response)
        self.import_props(obj)

        return self.getId()
