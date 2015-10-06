import json

from aolclient.models.base import Base


class Campaign(Base):

    def getId(self):
        return self.get('campaignId')

    def get_create_url(self):
        return '{0}/video-management/v1/organizations/{1}/advertisers/{2}/campaigns'.format(Base.connection.url, self.get('organization_id'), self.get('advertiser_id'))

    def get_by_advertiser(self, advertiser_id, organization_id):
        url = '{0}/video-management/v1/organizations/{1}/advertisers/{2}/campaigns'.format(Base.connection.url, organization_id, advertiser_id)
        method = "GET"

        response = self._execute(method, url, '')
        return self._get_response_objects(response)

