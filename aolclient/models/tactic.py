import json

from aolclient.models.base import Base

class Tactic(Base):

    obj_name = "tactics"

    def getId(self):
        return self.get('tacticId')

    def get_list_of_tactics(self, organization_id):
        url = '{0}/video-management/v1/organizations/{1}/advertisers/campaigns/tactics'.format(Base.connection.url, organization_id)
        method = 'GET'
        response = self._execute(method, url, '')
        return self._get_response_objects(response)

    def get_by_campaign(self, campaign_id, advertiser_id, organization_id):
        url = '{0}/video-management/v1/organizations/{1}/advertisers/{2}/campaigns/{3}/tactics'.format(Base.connection.url, organization_id, advertiser_id, campaign_id)
        method = "GET"

        response = self._execute(method, url, '')
        return self._get_response_objects(response)

    def get_by_id(self, organization_id, tactic_id, advertiser_id, campaign_id):
        url = '{0}/video-management/v1/organizations/{1}/advertisers/{2}/campaigns/{3}/tactics/{4}'.format(Base.connection.url, organization_id, advertiser_id, campaign_id, tactic_id)
        method = "GET"

        response = self._execute(method, url, '')
        return self._get_response_objects(response)
