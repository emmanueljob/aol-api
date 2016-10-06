import json

from aolclient.models.base import Base

from aolclient.service.connection import Connection

class Campaign(Base):

    obj_name = 'campaigns'

    def getBudget(self):
        # find the goal that is the total goal.
        if 'goals' in self:
            for goal in self['goals']:
                if goal['deliveryCappingType'] == 'GROSS_REVENUE' and goal['deliveryCappingResetPeriod'] == "TOTAL":
                    return goal['goal']
        return None

    def get_create_url(self):
        return '{0}/video-management/v2/organizations/{1}/advertisers/{2}/campaigns'.format(Base.connection.url, self.get('organization_id'), self.get('advertiser_id'))

    # get campaign by advertiser/org id
    def get_list_by_advertiser(self, advertiser_id, organization_id):
        url = '{0}/video-management/v2/organizations/{1}/advertisers/{2}/campaigns'.format(Base.connection.url, organization_id, advertiser_id)
        method = "GET"
        response = self._execute(method, url, '')
        return self._get_response_objects(response)

    # get campaigns by id
    def get_campaign_by_id(self, organization_id, advertiser_id, campaign_id):
        url = '{0}/video-management/v2/organizations/{1}/advertisers/{2}/campaigns/{3}'.format(Base.connection.url, organization_id, advertiser_id, campaign_id)
        method = 'GET'
        response = self._execute(method, url, '')
        return self._get_response_object(response)
