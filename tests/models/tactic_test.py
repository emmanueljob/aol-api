import unittest
import json

from aolclient.models.campaign import Campaign
from aolclient.models.tactic import Tactic
from tests.base import Base


class TacticTest(Base):

    def testGetByCampaign(self):
        
        loader = Campaign(TacticTest.conn)
        campaigns = loader.get_by_advertiser(25270, 11357)
        for test_campaign in campaigns:
            loader = Tactic(TacticTest.conn)
            tactics = loader.get_by_campaign(test_campaign.get('campaignId'), 25270, 11357)
            for tactic in tactics:
                print tactic
