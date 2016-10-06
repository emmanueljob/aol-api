import json

from aolclient.models.base import Base


class Advertiser(Base):

    obj_name = "advertiser"

    def getName(self):
        return self['globalAdvertiserName']

    def find_by_organization(self, organization_id, offset=0, limit=None):
        url = "{0}/video-management/v4/organizations/{1}/advertisers".format(Base.connection.url, organization_id)
        response = self._execute("GET", url, {})

        rval = []
        if response:
            rval = self._get_response_objects(response)
        return rval

    def find_by_id(self, organization_id, advertiser_id):
        url = "{0}/video-management/v1/organizations/{1}/advertisers/{2}".format(Base.connection.url, organization_id, advertiser_id)
        response = self._execute("GET", url, {})

        rval = []
        if response:
            rval = self._get_response_object(response)
        return rval

    
