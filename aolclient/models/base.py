import json
import requests
import time

class Base(dict):

    connection = None

    # Needs to be defined in the subclass
    obj_name = None

    def __init__(self, connection):
        Base.connection = connection
        super(Base, self).__init__()

    def get_url(self):
        return "{0}/{1}".format(Base.connection.url, self.obj_name)

    def get_create_url(self):
        print 'URL: ', self.get_url()
        return self.get_url()

    def get_find_url(self, id):
        return "{0}/{1}".format(self.get_url(), id)

    def find(self, id=None):
        if id is None:
            response = self._execute("GET", self.get_url(), None)

            rval = []
            if response:
                rval = self._get_response_objects(response)
            return rval
        else:
            print 'URL: ', self.get_find_url(id)
            response = self._execute("GET", self.get_find_url(id), None)
            print 'RESPONSE: ', response.text
            if response:
                return self._get_response_object(response)
            else:
                return None

    def create(self):
        if id in self:
            del self['id']

        print "CREATING!!!!!"

        response = self._execute("POST", self.get_create_url(), json.dumps(self.export_props()))
        obj = self._get_response_object(response)
        self.import_props(obj)

        return self.getId()

    def getId(self):
        return self.get('id')

    def getName(self):
        return self.get('name')

    def save(self):
        if self.getId() is None or self.getId() == 0:
            raise Exception("cant update an object with no id")

        response = self._execute("PUT", self.get_url(), json.dumps(self.export_props()))

        obj = self._get_response_object(response)
        self.import_props(obj)

        return self.getId()

    def _execute(self, method, url, payload):
        return self._execute_no_reauth(method, url, payload)

    def _execute_no_reauth(self, method, url, payload):

        headers = Base.connection.get_authorization()

        headers['Content-Type'] = 'application/json'

        print 'HEADERS AUTH: ', headers['Authorization']

        if method == "GET":
            print "curl -H 'Content-Type: application/json' -H 'Authorization: {0}' -d '{1}' '{2}'".format(headers['Authorization'], payload, url)
            start = time.time()
            rval = requests.get(url, headers=headers, data=payload, verify=False)
            total_time = time.time() - start
            print "TIME: " + str(total_time)
            print 'RVAL!!!: ', rval.text
            return rval
        elif method == "POST":
            print "curl -XPOST -H 'Content-Type: application/json' -H 'Authorization: {0}' -d '{1}' '{2}'".format(headers['Authorization'], payload, url)
            start = time.time()
            rval = requests.post(url, headers=headers, data=payload, verify=False)
            total_time = time.time() - start
            print "TIME: " + str(total_time)
            print rval.text
            return rval
        elif method == "PUT":
            print "curl -XPUT -H 'Content-Type: application/json' -H 'Authorization: {0}' -d '{1}' '{2}'".format(headers['Authorization'], payload, url)
            start = time.time()
            rval = requests.put(url, headers=headers, data=payload, verify=False)
            total_time = time.time() - start
            print "TIME: " + str(total_time)
            return rval
        elif method == "DELETE":
            start = time.time()
            rval = requests.delete(url, headers=headers)
            total_time = time.time() - start
            print "TIME: " + str(total_time)
            return rval
        else:
            raise Exception("Unknown method")

    def _get_response_objects(self, response):
        rval = []
        if response.status_code == 200:
            json_response = json.loads(response.text)
            print 'JSON RESPONSE: ', json_response
        else:
            print response.text
            raise Exception("Bad response code {0}".format(response.text))

        obj_list = []
        if 'list' in json_response:
            obj_list = json_response['list']

        else:
            obj_list = json_response
            rval.append(obj_list)
            return rval

        for obj in obj_list:
            new_obj = self.__class__(Base.connection)
            print 'NEW OBJ: ', new_obj
            new_obj.import_props(obj)
            rval.append(new_obj)

        return rval

    def _get_response_object(self, response):
        obj = json.loads(response.text)

        new_obj = None
        if obj and response.status_code in [200,201]:
            new_obj = self.__class__(Base.connection)
            new_obj.import_props(obj)
        else:
            print 'RESPONSE TEXT: ', response.text
            raise Exception("Bad response code: {0}  DATA: {1}".format(response.status_code, response.text))

        return new_obj

    def import_props(self, props):
        for key, value in props.iteritems():
            self[key] = value

    def export_props(self):
        rval = {}
        # do this an obvious way because using __dict__ gives us params we dont need.

        for key, value in self.iteritems():
            if key in ["advertiser_id", "organization_id"]:
                continue
            rval[key] = value

        print 'RVAL!!!!: ', json.dumps(rval)
        return rval
