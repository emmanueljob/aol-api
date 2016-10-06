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
        assert campaign_info is not None
        assert campaign_info.getBudget() > 0
        assert campaign_info.getId() > 0
        assert campaign_info.getName() is not None
