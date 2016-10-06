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
            assert result.getId() > 0
            assert result.getName() is not None

    def testGetById(self):
        loader = Advertiser(AdvertiserTest.conn)
        organization_id = 11357
        advertiser_id = 25270
        adv = loader.find_by_id(organization_id, advertiser_id)
        assert adv.getId() == advertiser_id
