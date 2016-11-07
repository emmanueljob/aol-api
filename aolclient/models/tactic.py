import json

from aolclient.models.base import Base

class Tactic(Base):

    obj_name = "tactics"

    def getName(self):
        return self.get('name')

    def setName(self, name):
        self['name'] = name

    def getCampaignId(self):
        return self.get('campaignId', 0)
    
    def getBudget(self):
        # find the goal that is the total goal.
        if 'goals' in self:
            for goal in self.get('goals'):
                if goal['deliveryCappingType'] == 'GROSS_REVENUE' and goal['deliveryCappingResetPeriod'] == "TOTAL":
                    return goal.get('goal')
        return None
    
    def setBudget(self, budget):
        # find the goal that is the total goal.
        if 'goals' not in self:
            self['goals'] = []
        added = False
        max_order = 0
        for goal in self.get('goals'):
            max_order = max(goal['ordering'], max_order)
            if goal['deliveryCappingType'] == 'GROSS_REVENUE' and goal['deliveryCappingResetPeriod'] == "TOTAL":
                added = True
                goal['goal'] = budget

        if not added:
            self['goals'].append({'deliveryCappingType': 'GROSS_REVENUE', 'deliveryCappingResetPeriod': "TOTAL", 'goal': budget, 'pacingType': 'LIMIT', 'ordering': max_order + 1})

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

        flights = self.get('flights')
        for flight in flights:
            del flight['id']

        goals = self.get('goals')
        for goal in goals:
            del goal['id']

        specification = self.get('specification')
        del specification['optimizationEnabled']
        del specification['nonLinearOverLay']
        del specification['notNonLinearOverLay']

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
            "priority": 1, #self.get('priority'),
            "alwaysDeliver": self.get('alwaysDeliver'),
            "aodBuyerMargin": self.get('aodBuyerMargin'),
            "aodPassthroughCost": self.get('aodPassthroughCost'),
            "pricingInformationType": self.get('pricingInformationType'),
            "cacheBreakers": self.get('cacheBreakers'),
            "specification": self.get('specification'),
            "flights": flights,
            "targeting": self.get('targeting'),
            "bid": self.get('bid'),
            "inventory": [
                {
                    "type": "DIRECTINVENTORY",
                    "priority": 1,
                    "items": inv_source_ids
                    }
                ],
            "medialist": self.get('medialist'),
            "goals": goals
            }

        response = self._execute(method, url, json.dumps(payload))
        print response.text
        return True

    def save(self, organization_id, advertiser_id):
        url = '{0}/video-management/v3/organizations/{1}/advertisers/{2}/campaigns/{3}/tactics/{4}'.format(Base.connection.url, organization_id, advertiser_id, self.getCampaignId(), self.getId())
        method = "PUT"

        flights = self.get('flights')
        for flight in flights:
            del flight['id']

        goals = self.get('goals')
        for goal in goals:
            if 'id' in goal:
                del goal['id']

        specification = self.get('specification')
        del specification['optimizationEnabled']
        del specification['nonLinearOverLay']
        del specification['notNonLinearOverLay']

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
            "priority": 1, #self.get('priority'),
            "alwaysDeliver": self.get('alwaysDeliver'),
            "aodBuyerMargin": self.get('aodBuyerMargin'),
            "aodPassthroughCost": self.get('aodPassthroughCost'),
            "pricingInformationType": self.get('pricingInformationType'),
            "cacheBreakers": self.get('cacheBreakers'),
            "specification": self.get('specification'),
            "flights": flights,
            "targeting": self.get('targeting'),
            "bid": self.get('bid'),
            "inventory": self.get('inventory'),
            "medialist": self.get('medialist'),
            "goals": goals
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
