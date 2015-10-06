import unittest
import json

from aolclient.models.campaign import Campaign
from aolclient.models.goal import Goal
from tests.base import Base


class GoalTest(Base):


    def testCreate(self):
        goal = Goal(GoalTest.conn)
        goal['advertiser_id'] = 25270
        goal['organization_id'] = 11357
        goal['campaign_id'] = 11357
        goal['name'] = "goal test"
        goal['startDate'] = "2014-10-17T00:00:00Z"
        goal['endDate'] = "2015-10-17T00:00:00Z"
        goal['status'] = "LIVE"
        # goal.create()
        

    def testGetByCampaign(self):
        
        loader = Campaign(GoalTest.conn)
        campaigns = loader.get_by_advertiser(25270, 11357)
        for test_campaign in campaigns:
            loader = Goal(GoalTest.conn)
            goals = loader.get_by_campaign(test_campaign.get('campaignId'), 25270, 11357)
            for goal in goals:
                print goal
