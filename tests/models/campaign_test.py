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
        campaign['name'] = "campaign test"
        campaign['startDate'] = "2014-10-17T00:00:00Z"
        campaign['endDate'] = "2015-10-17T00:00:00Z"
        campaign['status'] = "LIVE"
        # campaign.create()
        
    def testGetByAdvertiser(self):
        
        loader = Campaign(CampaignTest.conn)
        campaigns = loader.get_by_advertiser(25270, 11357)
        for test_campaign in campaigns:
            print test_campaign.get('campaignId')
