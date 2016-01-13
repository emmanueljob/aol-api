import unittest
import json

from aolclient.models.campaign import Campaign
from aolclient.models.advertiser import Advertiser
from tests.base import Base


class CampaignTest(Base):

    def testCreate(self):
        campaign = Campaign(CampaignTest.conn)
        campaign['advertiser_id'] = 25270
        campaign['organization_id'] = 11357
        campaign['name'] = "arun's campaign test"
        campaign['startDate'] = "2014-10-17T00:00:00Z"
        campaign['endDate'] = "2015-10-17T00:00:00Z"
        campaign['status'] = "LIVE"
        assert campaign.create() != None

    def testGetByCampaignId(self):
        campaign = Campaign(CampaignTest.conn)
        assert campaign.get_campaign_by_id('11357', '25270', '77527') == {u'status': u'LIVE', u'startDate': u'2014-10-17T00:00:00Z', u'endDate': u'2015-10-17T00:00:00Z', u'name': u"arun's campaign test", u'campaignId': 77527, u'organizationId': 11357, u'organizationSapId': 7000077134, u'currencyCode': None, u'advertiserId': 25270, u'customFieldValues': [], u'goals': [], u'advertiserSapId': 0}

    def testGetByAdvertiser(self):
        loader = Campaign(CampaignTest.conn)
        campaigns = loader.get_list_by_advertiser(25270, 11357)
        assert len(campaigns) >= 1

    def test_get_id(self):
        campaign = Campaign(CampaignTest.conn)
        campaignId = campaign.get_campaign_by_id('11357', '25270', '77061')['campaignId']
        assert campaignId == 77527
