import json

from aolclient.models.base import Base


class Advertiser(Base):

    obj_name = "advertiser"

    def find_by_organization(self, organization_id, offset=0, limit=None):
        url = "{0}/video-management/v1/organizations/{1}/advertisers".format(Base.connection.url, organization_id)
        response = self._execute("GET", url, {})

        rval = []
        if response:
            print "FIND FOUND"
            print response.text
            rval = self._get_response_objects(response)
        print response.text
        print "DONE"
        return rval
