import unittest
import json

from aolclient.models.advertiser import Advertiser
from tests.base import Base


class AdvertiserTest(Base):

    def testGetByOrganization(self):
        adv = Advertiser(AdvertiserTest.conn)
        organization_id = '11357'
        advs = adv.find_by_organization(organization_id)
        for result in advs:
            print result

