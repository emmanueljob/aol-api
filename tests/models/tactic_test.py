import json
import unittest

from aolclient.models.tactic import Tactic
from tests.base import Base


class TacticTest(Base):
        
    def test_get_by_campaign(self):
        campaign_id = 77061
        advertiser_id = 25270
        organization_id = 11357
        
        loader = Tactic(TacticTest.conn)
        tactics = loader.get_by_campaign(organization_id, advertiser_id, campaign_id)
        assert len(tactics) > 0

    def test_get_by_id(self):
        advertiser_id = 25270
        organization_id = 11357
        campaign_id = 77061
        tactic_id = 694407

        loader = Tactic(TacticTest.conn)
        tactic = loader.get_by_id(organization_id, advertiser_id, campaign_id, tactic_id)
        print tactic
        assert tactic.getId() == 694407
        assert tactic.getCampaignId() > 0
        # assert tactic.getBudget() > 0
        assert tactic.getStatus() > 0
        assert tactic.getStartDate() > 0
        assert tactic.getEndDate() > 0
        assert tactic.getFrequencyCap() > 0
        assert tactic.getFrequencyCapInterval() > 0
        assert tactic.getPrice() > 0

    def test_get_creatives(self):
        advertiser_id = 25270
        organization_id = 11357
        campaign_id = 77061
        tactic_id = 694407

        loader = Tactic(TacticTest.conn)
        tactic = loader.get_by_id(organization_id, advertiser_id, campaign_id, tactic_id)
        assert tactic.getId() == 694407
        creatives = tactic.get_creatives(organization_id, advertiser_id)
        assert len(creatives) == 1

    def test_get_deals(self):
        advertiser_id = 25270
        organization_id = 11357
        campaign_id = 77061
        tactic_id = 694407
        deal_ids = [710850]

        loader = Tactic(TacticTest.conn)
        tactic = loader.get_by_id(organization_id, advertiser_id, campaign_id, tactic_id)
        assert tactic.getId() == 694407
        assert tactic.set_inventory_sources(deal_ids, organization_id, advertiser_id)
        tactic = loader.get_by_id(organization_id, advertiser_id, campaign_id, tactic_id)
        print json.dumps(tactic, indent=4)
        assert len(tactic.get_inventory_sources()) == 1

        
