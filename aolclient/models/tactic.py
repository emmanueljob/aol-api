import json

from aolclient.models.base import Base

class Tactic(Base):

    obj_name = "tactics"
    
    def getCampaignId(self):
        return self.get('campaignId', 0)
    
    def getBudget(self):
        # find the goal that is the total goal.
        if 'goals' in self:
            for goal in self.get('goals'):
                if goal['deliveryCappingType'] == 'GROSS_REVENUE' and goal['deliveryCappingResetPeriod'] == "TOTAL":
                    return goal.get('goal')
        return None

    def getActive(self):
        pass
    
    def getStatus(self):
        return self.get('status')

    def getDeals(self):
        return []

    def getStartDate(self):
        return self.get('servingStartDate')

    def getEndDate(self):
        return self.get('servingEndDate')

    def getEndDate(self):
        return self.get('servingEndDate')

    def getFrequencyCap(self):
        return self.get('frequencyCappingAmount')

    def getFrequencyCapInterval(self):
        return self.get('frequencyCappingResetPeriod')

    def getPrice(self):
        return self.get('price')

    def get_by_campaign(self, organization_id, advertiser_id, campaign_id):
        url = '{0}/video-management/v3/organizations/{1}/advertisers/{2}/campaigns/{3}/tactics'.format(Base.connection.url, organization_id, advertiser_id, campaign_id)
        method = "GET"
        response = self._execute(method, url, '')
        return self._get_response_objects(response)

    def get_by_id(self, organization_id, advertiser_id, campaign_id, tactic_id):
        url = '{0}/video-management/v3/organizations/{1}/advertisers/{2}/campaigns/{3}/tactics/{4}'.format(Base.connection.url, organization_id, advertiser_id, campaign_id, tactic_id)
        method = "GET"
        response = self._execute(method, url, '')
        return self._get_response_object(response)

    def get_creatives(self, organization_id, advertiser_id):
        url = '{0}/video-management/v2/organizations/{1}/advertisers/{2}/creatives?tacticId={3}'.format(Base.connection.url, organization_id, advertiser_id, self.getId())
        method = "GET"
        response = self._execute(method, url, '')
        return self._get_creative_response_objects(response)

    def get_inventory_sources(self):
        return self.get('inventory')

    def set_inventory_sources(self, inv_source_ids, organization_id, advertiser_id):
        url = '{0}/video-management/v3/organizations/{1}/advertisers/{2}/campaigns/{3}/tactics/{4}'.format(Base.connection.url, organization_id, advertiser_id, self.getCampaignId(), self.getId())
        method = "PUT"

        payload = {
            "name": self.get('name'),
            "description": self.get('description'),
            "frequencyCappingAmount": self.get('frequencyCappingAmount'),
            "frequencyCappingResetPeriod": self.get('frequencyCappingResetPeriod'),
            "cost": self.get('cost'),
            "price": self.get('price'),
            "pricingType": self.get('pricingType'),
            "deliveryAlgorithmType": self.get('deliveryAlgorithmType'),
            "deliveryCatchUpSpeed": self.get('deliveryCatchUpSpeed'),
            "status": self.get('status'),
            "adType": self.get('adType'),
            "priority": self.get('priority'),
            "alwaysDeliver": self.get('alwaysDeliver'),
            "aodBuyerMargin": self.get('aodBuyerMargin'),
            "aodPassthroughCost": self.get('aodPassthroughCost'),
            "pricingInformationType": self.get('pricingInformationType'),
            "cacheBreakers": self.get('cacheBreakers'),
            "specification": self.get('specification'),
            "flights": self.get('flights'),
            "targeting": self.get('targeting'),
            "bid": self.get('bid'),
            "inventory": [
                {
                    "type": "DIRECTINVENTORY",
                    "priority": 0,
                    "items": inv_source_ids
                    }
                ],
            "medialist": self.get('medialist'),
            "goals": self.get('goals')
            }

        response = self._execute(method, url, json.dumps(payload))
        print response.text
        return True



    def _get_creative_response_objects(self, response):
        rval = []
        json_response = None
        if response.status_code == 200:
            json_response = json.loads(response.text)
        else:
            print response.text
            raise Exception("Bad response code {0}".format(response.text))

        obj_list = []
        if 'data' in json_response:
            for key, value in json_response['data'].iteritems():
                obj_list = obj_list + value

        for obj in obj_list:
            new_obj = self.__class__(Base.connection)
            new_obj.import_props(obj)
            rval.append(new_obj)

        return rval
