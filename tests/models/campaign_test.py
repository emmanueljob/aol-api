import unittest
import json

from aolclient.models.campaign import Campaign
from aolclient.models.advertiser import Advertiser
from tests.base import Base

class CampaignTest(Base):

    def test_get_create_url(self):
        campaign_instance = Campaign(CampaignTest.conn)
        assert campaign_instance.get_create_url() == 'https://sandbox.video.advertising.aol.com/peach-rest-api/video-management/v2/organizations/None/advertisers/None/campaigns'

    def test_get_list_by_advertiser(self):
        loader = Campaign(CampaignTest.conn)
        campaigns = loader.get_list_by_advertiser(25270, 11357)
        campaign_ids = []
        for campaign in campaigns:
            campaign_ids.append(campaign.getId())
        assert 77061 in campaign_ids

    def test_get_campaign_by_id(self):
        campaign = Campaign(CampaignTest.conn)
        campaign_info = campaign.get_campaign_by_id(11357, 25270, 77061)
        assert campaign_info == {u'fcapAmount': 0, u'status': u'LIVE', u'conversionEvents': [], u'createdFromAuction': False, u'name': u'Hiscox American Courage Q3', u'fcapResetPeriod': 0, u'servingEndDate': u'2015-10-10T23:59:00-0700', u'organizationSapId': 7000077134, u'currencyCode': u'USD', u'apps': [{u'campaignAppStatus': u'READY', u'appName': u'ONE by AOL: Video Viewability Targeting and Optimization', u'logoUrl': u'http://cdn.adap.tv/rona/one-by-aol-04132015114756-175.png', u'feeInfo': u'Free', u'appId': 16}], u'brandId': 19390, u'flights': [{u'startDate': u'2015-09-08T00:00:00-0700', u'endDate': u'2015-10-10T23:59:00-0700', u'id': 127238}], u'brandName': u'American Courage', u'apertureEnabled': False, u'goals': [{u'goal': 57000.0, u'campaignId': 77061, u'deliveryCappingResetPeriod': u'TOTAL', u'ordering': 1, u'deliveryCappingType': u'GROSS_REVENUE', u'id': 31341}], u'advertiserSapId': 0, u'servingStartDate': u'2015-09-08T00:00:00-0700', u'id': 77061}
