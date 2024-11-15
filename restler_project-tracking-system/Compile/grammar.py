""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_app_api_assignments_post_commitDate = dependencies.DynamicVariable("_app_api_assignments_post_commitDate")

_app_api_assignments_post_commitEmpDesc = dependencies.DynamicVariable("_app_api_assignments_post_commitEmpDesc")

_app_api_assignments_post_commitMgrDesc = dependencies.DynamicVariable("_app_api_assignments_post_commitMgrDesc")

_app_api_assignments_post_employeeId = dependencies.DynamicVariable("_app_api_assignments_post_employeeId")

_app_api_assignments_post_projectId = dependencies.DynamicVariable("_app_api_assignments_post_projectId")

_app_api_assignments_put_employee_employeeId = dependencies.DynamicVariable("_app_api_assignments_put_employee_employeeId")

_app_api_credentials_post_credentialId = dependencies.DynamicVariable("_app_api_credentials_post_credentialId")

_app_api_credentials_post_enabled = dependencies.DynamicVariable("_app_api_credentials_post_enabled")

_app_api_credentials_post_password = dependencies.DynamicVariable("_app_api_credentials_post_password")

_app_api_credentials_post_role = dependencies.DynamicVariable("_app_api_credentials_post_role")

_app_api_credentials_post_username = dependencies.DynamicVariable("_app_api_credentials_post_username")

_app_api_departments_post_departmentId = dependencies.DynamicVariable("_app_api_departments_post_departmentId")

_app_api_departments_post_departmentName = dependencies.DynamicVariable("_app_api_departments_post_departmentName")

_app_api_locations_post_adr = dependencies.DynamicVariable("_app_api_locations_post_adr")

_app_api_locations_post_city = dependencies.DynamicVariable("_app_api_locations_post_city")

_app_api_locations_post_locationId = dependencies.DynamicVariable("_app_api_locations_post_locationId")

_app_api_locations_post_postalCode = dependencies.DynamicVariable("_app_api_locations_post_postalCode")

_app_api_projects_post_endDate = dependencies.DynamicVariable("_app_api_projects_post_endDate")

_app_api_projects_post_projectId = dependencies.DynamicVariable("_app_api_projects_post_projectId")

_app_api_projects_post_startDate = dependencies.DynamicVariable("_app_api_projects_post_startDate")

_app_api_projects_post_status = dependencies.DynamicVariable("_app_api_projects_post_status")

_app_api_projects_post_title = dependencies.DynamicVariable("_app_api_projects_post_title")

_app_api_projects_put_endDate = dependencies.DynamicVariable("_app_api_projects_put_endDate")

_app_api_projects_put_projectId = dependencies.DynamicVariable("_app_api_projects_put_projectId")

_app_api_projects_put_startDate = dependencies.DynamicVariable("_app_api_projects_put_startDate")

_app_api_projects_put_status = dependencies.DynamicVariable("_app_api_projects_put_status")

_app_api_projects_put_title = dependencies.DynamicVariable("_app_api_projects_put_title")

def parse_appapiassignmentspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None
    temp_8173 = None
    temp_7680 = None
    temp_5581 = None
    temp_2060 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7262 = str(data["commitDate"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8173 = str(data["commitEmpDesc"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_7680 = str(data["commitMgrDesc"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5581 = str(data["employeeId"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2060 = str(data["projectId"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7262 or temp_8173 or temp_7680 or temp_5581 or temp_2060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_app_api_assignments_post_commitDate", temp_7262)
    if temp_8173:
        dependencies.set_variable("_app_api_assignments_post_commitEmpDesc", temp_8173)
    if temp_7680:
        dependencies.set_variable("_app_api_assignments_post_commitMgrDesc", temp_7680)
    if temp_5581:
        dependencies.set_variable("_app_api_assignments_post_employeeId", temp_5581)
    if temp_2060:
        dependencies.set_variable("_app_api_assignments_post_projectId", temp_2060)


def parse_appapiassignmentsput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_5588 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_5588 = str(data["employee"]["employeeId"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5588):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5588:
        dependencies.set_variable("_app_api_assignments_put_employee_employeeId", temp_5588)


def parse_appapicredentialspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9060 = None
    temp_4421 = None
    temp_9775 = None
    temp_2737 = None
    temp_2919 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_9060 = str(data["credentialId"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_4421 = str(data["enabled"])
            temp_4421 = temp_4421.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9775 = str(data["password"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2737 = str(data["role"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2919 = str(data["username"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9060 or temp_4421 or temp_9775 or temp_2737 or temp_2919):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9060:
        dependencies.set_variable("_app_api_credentials_post_credentialId", temp_9060)
    if temp_4421:
        dependencies.set_variable("_app_api_credentials_post_enabled", temp_4421)
    if temp_9775:
        dependencies.set_variable("_app_api_credentials_post_password", temp_9775)
    if temp_2737:
        dependencies.set_variable("_app_api_credentials_post_role", temp_2737)
    if temp_2919:
        dependencies.set_variable("_app_api_credentials_post_username", temp_2919)


def parse_appapidepartmentspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_4673 = None
    temp_6326 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_4673 = str(data["departmentId"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6326 = str(data["departmentName"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4673 or temp_6326):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4673:
        dependencies.set_variable("_app_api_departments_post_departmentId", temp_4673)
    if temp_6326:
        dependencies.set_variable("_app_api_departments_post_departmentName", temp_6326)


def parse_appapilocationspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_4695 = None
    temp_9821 = None
    temp_303 = None
    temp_8623 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_4695 = str(data["adr"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9821 = str(data["city"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_303 = str(data["locationId"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8623 = str(data["postalCode"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4695 or temp_9821 or temp_303 or temp_8623):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4695:
        dependencies.set_variable("_app_api_locations_post_adr", temp_4695)
    if temp_9821:
        dependencies.set_variable("_app_api_locations_post_city", temp_9821)
    if temp_303:
        dependencies.set_variable("_app_api_locations_post_locationId", temp_303)
    if temp_8623:
        dependencies.set_variable("_app_api_locations_post_postalCode", temp_8623)


def parse_appapiprojectspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9953 = None
    temp_6771 = None
    temp_3145 = None
    temp_8169 = None
    temp_8480 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_9953 = str(data["endDate"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6771 = str(data["projectId"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_3145 = str(data["startDate"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8169 = str(data["status"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8480 = str(data["title"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9953 or temp_6771 or temp_3145 or temp_8169 or temp_8480):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9953:
        dependencies.set_variable("_app_api_projects_post_endDate", temp_9953)
    if temp_6771:
        dependencies.set_variable("_app_api_projects_post_projectId", temp_6771)
    if temp_3145:
        dependencies.set_variable("_app_api_projects_post_startDate", temp_3145)
    if temp_8169:
        dependencies.set_variable("_app_api_projects_post_status", temp_8169)
    if temp_8480:
        dependencies.set_variable("_app_api_projects_post_title", temp_8480)


def parse_appapiprojectsput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9919 = None
    temp_326 = None
    temp_6999 = None
    temp_5262 = None
    temp_9340 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_9919 = str(data["endDate"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_326 = str(data["projectId"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6999 = str(data["startDate"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5262 = str(data["status"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9340 = str(data["title"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9919 or temp_326 or temp_6999 or temp_5262 or temp_9340):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9919:
        dependencies.set_variable("_app_api_projects_put_endDate", temp_9919)
    if temp_326:
        dependencies.set_variable("_app_api_projects_put_projectId", temp_326)
    if temp_6999:
        dependencies.set_variable("_app_api_projects_put_startDate", temp_6999)
    if temp_5262:
        dependencies.set_variable("_app_api_projects_put_status", temp_5262)
    if temp_9340:
        dependencies.set_variable("_app_api_projects_put_title", temp_9340)

req_collection = requests.RequestCollection([])
# Endpoint: /app/api/assignments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/assignments"
)
req_collection.add_request(request)

# Endpoint: /app/api/assignments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "commitDate":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["dd-MM-yyyyHH:mm:ss"]),
    primitives.restler_static_string(""",
    "commitEmpDesc":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "commitMgrDesc":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "employee":
        {
            "credential":
                {
                    "credentialId":"""),
    primitives.restler_static_string(_app_api_credentials_post_credentialId.reader(), quoted=False),
    primitives.restler_static_string(""",
                    "enabled":"""),
    primitives.restler_static_string(_app_api_credentials_post_enabled.reader(), quoted=False),
    primitives.restler_static_string(""",
                    "password":"""),
    primitives.restler_static_string(_app_api_credentials_post_password.reader(), quoted=True),
    primitives.restler_static_string(""",
                    "role":"""),
    primitives.restler_static_string(_app_api_credentials_post_role.reader(), quoted=True),
    primitives.restler_static_string(""",
                    "username":"""),
    primitives.restler_static_string(_app_api_credentials_post_username.reader(), quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "department":
                {
                    "departmentId":"""),
    primitives.restler_static_string(_app_api_departments_post_departmentId.reader(), quoted=False),
    primitives.restler_static_string(""",
                    "departmentName":"""),
    primitives.restler_static_string(_app_api_departments_post_departmentName.reader(), quoted=True),
    primitives.restler_static_string(""",
                    "location":
                        {
                            "adr":"""),
    primitives.restler_static_string(_app_api_locations_post_adr.reader(), quoted=True),
    primitives.restler_static_string(""",
                            "city":"""),
    primitives.restler_static_string(_app_api_locations_post_city.reader(), quoted=True),
    primitives.restler_static_string(""",
                            "locationId":"""),
    primitives.restler_static_string(_app_api_locations_post_locationId.reader(), quoted=False),
    primitives.restler_static_string(""",
                            "postalCode":"""),
    primitives.restler_static_string(_app_api_locations_post_postalCode.reader(), quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "employeeId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "firstName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "hiredate":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["dd-MM-yyyy"]),
    primitives.restler_static_string(""",
            "job":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "lastName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "manager":
                """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
            ,
            "phone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "salary":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("""
        }
    ,
    "employeeId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "project":
        {
            "endDate":"""),
    primitives.restler_static_string(_app_api_projects_put_endDate.reader(), quoted=True),
    primitives.restler_static_string(""",
            "projectId":"""),
    primitives.restler_static_string(_app_api_projects_put_projectId.reader(), quoted=False),
    primitives.restler_static_string(""",
            "startDate":"""),
    primitives.restler_static_string(_app_api_projects_put_startDate.reader(), quoted=True),
    primitives.restler_static_string(""",
            "status":"""),
    primitives.restler_static_string(_app_api_projects_put_status.reader(), quoted=True),
    primitives.restler_static_string(""",
            "title":"""),
    primitives.restler_static_string(_app_api_projects_put_title.reader(), quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "projectId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_appapiassignmentspost,
            'dependencies':
            [
                _app_api_assignments_post_commitDate.writer(),
                _app_api_assignments_post_commitEmpDesc.writer(),
                _app_api_assignments_post_commitMgrDesc.writer(),
                _app_api_assignments_post_employeeId.writer(),
                _app_api_assignments_post_projectId.writer()
            ]
        }

    },

],
requestId="/app/api/assignments"
)
req_collection.add_request(request)

# Endpoint: /app/api/assignments, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "commitDate":"""),
    primitives.restler_static_string(_app_api_assignments_post_commitDate.reader(), quoted=True),
    primitives.restler_static_string(""",
    "commitEmpDesc":"""),
    primitives.restler_static_string(_app_api_assignments_post_commitEmpDesc.reader(), quoted=True),
    primitives.restler_static_string(""",
    "commitMgrDesc":"""),
    primitives.restler_static_string(_app_api_assignments_post_commitMgrDesc.reader(), quoted=True),
    primitives.restler_static_string(""",
    "employee":
        {
            "credential":
                {
                    "credentialId":"""),
    primitives.restler_static_string(_app_api_credentials_post_credentialId.reader(), quoted=False),
    primitives.restler_static_string(""",
                    "enabled":"""),
    primitives.restler_static_string(_app_api_credentials_post_enabled.reader(), quoted=False),
    primitives.restler_static_string(""",
                    "password":"""),
    primitives.restler_static_string(_app_api_credentials_post_password.reader(), quoted=True),
    primitives.restler_static_string(""",
                    "role":"""),
    primitives.restler_static_string(_app_api_credentials_post_role.reader(), quoted=True),
    primitives.restler_static_string(""",
                    "username":"""),
    primitives.restler_static_string(_app_api_credentials_post_username.reader(), quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "department":
                {
                    "departmentId":"""),
    primitives.restler_static_string(_app_api_departments_post_departmentId.reader(), quoted=False),
    primitives.restler_static_string(""",
                    "departmentName":"""),
    primitives.restler_static_string(_app_api_departments_post_departmentName.reader(), quoted=True),
    primitives.restler_static_string(""",
                    "location":
                        {
                            "adr":"""),
    primitives.restler_static_string(_app_api_locations_post_adr.reader(), quoted=True),
    primitives.restler_static_string(""",
                            "city":"""),
    primitives.restler_static_string(_app_api_locations_post_city.reader(), quoted=True),
    primitives.restler_static_string(""",
                            "locationId":"""),
    primitives.restler_static_string(_app_api_locations_post_locationId.reader(), quoted=False),
    primitives.restler_static_string(""",
                            "postalCode":"""),
    primitives.restler_static_string(_app_api_locations_post_postalCode.reader(), quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "employeeId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "firstName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "hiredate":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["dd-MM-yyyy"]),
    primitives.restler_static_string(""",
            "job":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "lastName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "manager":
                """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
            ,
            "phone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "salary":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("""
        }
    ,
    "employeeId":"""),
    primitives.restler_static_string(_app_api_assignments_post_employeeId.reader(), quoted=False),
    primitives.restler_static_string(""",
    "project":
        {
            "endDate":"""),
    primitives.restler_static_string(_app_api_projects_put_endDate.reader(), quoted=True),
    primitives.restler_static_string(""",
            "projectId":"""),
    primitives.restler_static_string(_app_api_projects_put_projectId.reader(), quoted=False),
    primitives.restler_static_string(""",
            "startDate":"""),
    primitives.restler_static_string(_app_api_projects_put_startDate.reader(), quoted=True),
    primitives.restler_static_string(""",
            "status":"""),
    primitives.restler_static_string(_app_api_projects_put_status.reader(), quoted=True),
    primitives.restler_static_string(""",
            "title":"""),
    primitives.restler_static_string(_app_api_projects_put_title.reader(), quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "projectId":"""),
    primitives.restler_static_string(_app_api_assignments_post_projectId.reader(), quoted=False),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_appapiassignmentsput,
            'dependencies':
            [
                _app_api_assignments_put_employee_employeeId.writer()
            ]
        }

    },

],
requestId="/app/api/assignments"
)
req_collection.add_request(request)

# Endpoint: /app/api/assignments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/assignments"
)
req_collection.add_request(request)

# Endpoint: /app/api/assignments/data/project-commit/{employeeId}/{projectId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("data"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("project-commit"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/assignments/data/project-commit/{employeeId}/{projectId}"
)
req_collection.add_request(request)

# Endpoint: /app/api/assignments/data/project-commit/{employeeId}/{projectId}/{commitDate}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("data"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("project-commit"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/assignments/data/project-commit/{employeeId}/{projectId}/{commitDate}"
)
req_collection.add_request(request)

# Endpoint: /app/api/assignments/data/project-commit/{projectId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("data"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("project-commit"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/assignments/data/project-commit/{projectId}"
)
req_collection.add_request(request)

# Endpoint: /app/api/assignments/delete/{employeeId}/{projectId}/{commitDate}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("delete"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/assignments/delete/{employeeId}/{projectId}/{commitDate}"
)
req_collection.add_request(request)

# Endpoint: /app/api/assignments/save, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("save"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "commitDate":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["dd-MM-yyyyHH:mm:ss"]),
    primitives.restler_static_string(""",
    "commitEmpDesc":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "commitMgrDesc":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "employee":
        {
            "credential":
                {
                    "credentialId":"""),
    primitives.restler_static_string(_app_api_credentials_post_credentialId.reader(), quoted=False),
    primitives.restler_static_string(""",
                    "enabled":"""),
    primitives.restler_static_string(_app_api_credentials_post_enabled.reader(), quoted=False),
    primitives.restler_static_string(""",
                    "password":"""),
    primitives.restler_static_string(_app_api_credentials_post_password.reader(), quoted=True),
    primitives.restler_static_string(""",
                    "role":"""),
    primitives.restler_static_string(_app_api_credentials_post_role.reader(), quoted=True),
    primitives.restler_static_string(""",
                    "username":"""),
    primitives.restler_static_string(_app_api_credentials_post_username.reader(), quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "department":
                {
                    "departmentId":"""),
    primitives.restler_static_string(_app_api_departments_post_departmentId.reader(), quoted=False),
    primitives.restler_static_string(""",
                    "departmentName":"""),
    primitives.restler_static_string(_app_api_departments_post_departmentName.reader(), quoted=True),
    primitives.restler_static_string(""",
                    "location":
                        {
                            "adr":"""),
    primitives.restler_static_string(_app_api_locations_post_adr.reader(), quoted=True),
    primitives.restler_static_string(""",
                            "city":"""),
    primitives.restler_static_string(_app_api_locations_post_city.reader(), quoted=True),
    primitives.restler_static_string(""",
                            "locationId":"""),
    primitives.restler_static_string(_app_api_locations_post_locationId.reader(), quoted=False),
    primitives.restler_static_string(""",
                            "postalCode":"""),
    primitives.restler_static_string(_app_api_locations_post_postalCode.reader(), quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "employeeId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "firstName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "hiredate":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["dd-MM-yyyy"]),
    primitives.restler_static_string(""",
            "job":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "lastName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "manager":
                """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
            ,
            "phone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "salary":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("""
        }
    ,
    "employeeId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "project":
        {
            "endDate":"""),
    primitives.restler_static_string(_app_api_projects_put_endDate.reader(), quoted=True),
    primitives.restler_static_string(""",
            "projectId":"""),
    primitives.restler_static_string(_app_api_projects_put_projectId.reader(), quoted=False),
    primitives.restler_static_string(""",
            "startDate":"""),
    primitives.restler_static_string(_app_api_projects_put_startDate.reader(), quoted=True),
    primitives.restler_static_string(""",
            "status":"""),
    primitives.restler_static_string(_app_api_projects_put_status.reader(), quoted=True),
    primitives.restler_static_string(""",
            "title":"""),
    primitives.restler_static_string(_app_api_projects_put_title.reader(), quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "projectId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/assignments/save"
)
req_collection.add_request(request)

# Endpoint: /app/api/assignments/update, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("update"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "commitDate":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["dd-MM-yyyyHH:mm:ss"]),
    primitives.restler_static_string(""",
    "commitEmpDesc":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "commitMgrDesc":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "employee":
        {
            "credential":
                {
                    "credentialId":"""),
    primitives.restler_static_string(_app_api_credentials_post_credentialId.reader(), quoted=False),
    primitives.restler_static_string(""",
                    "enabled":"""),
    primitives.restler_static_string(_app_api_credentials_post_enabled.reader(), quoted=False),
    primitives.restler_static_string(""",
                    "password":"""),
    primitives.restler_static_string(_app_api_credentials_post_password.reader(), quoted=True),
    primitives.restler_static_string(""",
                    "role":"""),
    primitives.restler_static_string(_app_api_credentials_post_role.reader(), quoted=True),
    primitives.restler_static_string(""",
                    "username":"""),
    primitives.restler_static_string(_app_api_credentials_post_username.reader(), quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "department":
                {
                    "departmentId":"""),
    primitives.restler_static_string(_app_api_departments_post_departmentId.reader(), quoted=False),
    primitives.restler_static_string(""",
                    "departmentName":"""),
    primitives.restler_static_string(_app_api_departments_post_departmentName.reader(), quoted=True),
    primitives.restler_static_string(""",
                    "location":
                        {
                            "adr":"""),
    primitives.restler_static_string(_app_api_locations_post_adr.reader(), quoted=True),
    primitives.restler_static_string(""",
                            "city":"""),
    primitives.restler_static_string(_app_api_locations_post_city.reader(), quoted=True),
    primitives.restler_static_string(""",
                            "locationId":"""),
    primitives.restler_static_string(_app_api_locations_post_locationId.reader(), quoted=False),
    primitives.restler_static_string(""",
                            "postalCode":"""),
    primitives.restler_static_string(_app_api_locations_post_postalCode.reader(), quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "employeeId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "firstName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "hiredate":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["dd-MM-yyyy"]),
    primitives.restler_static_string(""",
            "job":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "lastName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "manager":
                """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
            ,
            "phone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "salary":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string("""
        }
    ,
    "employeeId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "project":
        {
            "endDate":"""),
    primitives.restler_static_string(_app_api_projects_put_endDate.reader(), quoted=True),
    primitives.restler_static_string(""",
            "projectId":"""),
    primitives.restler_static_string(_app_api_projects_put_projectId.reader(), quoted=False),
    primitives.restler_static_string(""",
            "startDate":"""),
    primitives.restler_static_string(_app_api_projects_put_startDate.reader(), quoted=True),
    primitives.restler_static_string(""",
            "status":"""),
    primitives.restler_static_string(_app_api_projects_put_status.reader(), quoted=True),
    primitives.restler_static_string(""",
            "title":"""),
    primitives.restler_static_string(_app_api_projects_put_title.reader(), quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "projectId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/assignments/update"
)
req_collection.add_request(request)

# Endpoint: /app/api/assignments/{employeeId}/{projectId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_app_api_assignments_put_employee_employeeId.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/assignments/{employeeId}/{projectId}"
)
req_collection.add_request(request)

# Endpoint: /app/api/assignments/{employeeId}/{projectId}/{commitDate}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_app_api_assignments_put_employee_employeeId.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/assignments/{employeeId}/{projectId}/{commitDate}"
)
req_collection.add_request(request)

# Endpoint: /app/api/assignments/{employeeId}/{projectId}/{commitDate}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_app_api_assignments_put_employee_employeeId.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/assignments/{employeeId}/{projectId}/{commitDate}"
)
req_collection.add_request(request)

# Endpoint: /app/api/authenticate, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("authenticate"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/authenticate"
)
req_collection.add_request(request)

# Endpoint: /app/api/authenticate, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("authenticate"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/authenticate"
)
req_collection.add_request(request)

# Endpoint: /app/api/credentials, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credentials"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/credentials"
)
req_collection.add_request(request)

# Endpoint: /app/api/credentials, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credentials"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "credentialId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "enabled":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_appapicredentialspost,
            'dependencies':
            [
                _app_api_credentials_post_credentialId.writer(),
                _app_api_credentials_post_enabled.writer(),
                _app_api_credentials_post_password.writer(),
                _app_api_credentials_post_role.writer(),
                _app_api_credentials_post_username.writer()
            ]
        }

    },

],
requestId="/app/api/credentials"
)
req_collection.add_request(request)

# Endpoint: /app/api/credentials, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credentials"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "credentialId":"""),
    primitives.restler_static_string(_app_api_credentials_post_credentialId.reader(), quoted=False),
    primitives.restler_static_string(""",
    "enabled":"""),
    primitives.restler_static_string(_app_api_credentials_post_enabled.reader(), quoted=False),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_static_string(_app_api_credentials_post_password.reader(), quoted=True),
    primitives.restler_static_string(""",
    "role":"""),
    primitives.restler_static_string(_app_api_credentials_post_role.reader(), quoted=True),
    primitives.restler_static_string(""",
    "username":"""),
    primitives.restler_static_string(_app_api_credentials_post_username.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/credentials"
)
req_collection.add_request(request)

# Endpoint: /app/api/credentials, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credentials"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("credentialId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/credentials"
)
req_collection.add_request(request)

# Endpoint: /app/api/credentials, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credentials"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/credentials"
)
req_collection.add_request(request)

# Endpoint: /app/api/credentials/delete, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credentials"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("delete"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("credentialId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/credentials/delete"
)
req_collection.add_request(request)

# Endpoint: /app/api/credentials/save, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credentials"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("save"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "credentialId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "enabled":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/credentials/save"
)
req_collection.add_request(request)

# Endpoint: /app/api/credentials/update, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credentials"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("update"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "credentialId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "enabled":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "role":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/credentials/update"
)
req_collection.add_request(request)

# Endpoint: /app/api/credentials/username/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credentials"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("username"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/credentials/username/{username}"
)
req_collection.add_request(request)

# Endpoint: /app/api/credentials/username/{username}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credentials"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("username"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/credentials/username/{username}"
)
req_collection.add_request(request)

# Endpoint: /app/api/credentials/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("credentials"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/credentials/{id}"
)
req_collection.add_request(request)

# Endpoint: /app/api/departments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("departments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/departments"
)
req_collection.add_request(request)

# Endpoint: /app/api/departments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("departments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "departmentId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "departmentName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "location":
        {
            "adr":"""),
    primitives.restler_static_string(_app_api_locations_post_adr.reader(), quoted=True),
    primitives.restler_static_string(""",
            "city":"""),
    primitives.restler_static_string(_app_api_locations_post_city.reader(), quoted=True),
    primitives.restler_static_string(""",
            "locationId":"""),
    primitives.restler_static_string(_app_api_locations_post_locationId.reader(), quoted=False),
    primitives.restler_static_string(""",
            "postalCode":"""),
    primitives.restler_static_string(_app_api_locations_post_postalCode.reader(), quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_appapidepartmentspost,
            'dependencies':
            [
                _app_api_departments_post_departmentId.writer(),
                _app_api_departments_post_departmentName.writer()
            ]
        }

    },

],
requestId="/app/api/departments"
)
req_collection.add_request(request)

# Endpoint: /app/api/departments, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("departments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "departmentId":"""),
    primitives.restler_static_string(_app_api_departments_post_departmentId.reader(), quoted=False),
    primitives.restler_static_string(""",
    "departmentName":"""),
    primitives.restler_static_string(_app_api_departments_post_departmentName.reader(), quoted=True),
    primitives.restler_static_string(""",
    "location":
        {
            "adr":"""),
    primitives.restler_static_string(_app_api_locations_post_adr.reader(), quoted=True),
    primitives.restler_static_string(""",
            "city":"""),
    primitives.restler_static_string(_app_api_locations_post_city.reader(), quoted=True),
    primitives.restler_static_string(""",
            "locationId":"""),
    primitives.restler_static_string(_app_api_locations_post_locationId.reader(), quoted=False),
    primitives.restler_static_string(""",
            "postalCode":"""),
    primitives.restler_static_string(_app_api_locations_post_postalCode.reader(), quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/departments"
)
req_collection.add_request(request)

# Endpoint: /app/api/departments, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("departments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("departmentId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/departments"
)
req_collection.add_request(request)

# Endpoint: /app/api/departments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("departments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/departments"
)
req_collection.add_request(request)

# Endpoint: /app/api/departments/delete, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("departments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("delete"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("departmentId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/departments/delete"
)
req_collection.add_request(request)

# Endpoint: /app/api/departments/save, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("departments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("save"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "departmentId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "departmentName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "location":
        {
            "adr":"""),
    primitives.restler_static_string(_app_api_locations_post_adr.reader(), quoted=True),
    primitives.restler_static_string(""",
            "city":"""),
    primitives.restler_static_string(_app_api_locations_post_city.reader(), quoted=True),
    primitives.restler_static_string(""",
            "locationId":"""),
    primitives.restler_static_string(_app_api_locations_post_locationId.reader(), quoted=False),
    primitives.restler_static_string(""",
            "postalCode":"""),
    primitives.restler_static_string(_app_api_locations_post_postalCode.reader(), quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/departments/save"
)
req_collection.add_request(request)

# Endpoint: /app/api/departments/update, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("departments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("update"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "departmentId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "departmentName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "location":
        {
            "adr":"""),
    primitives.restler_static_string(_app_api_locations_post_adr.reader(), quoted=True),
    primitives.restler_static_string(""",
            "city":"""),
    primitives.restler_static_string(_app_api_locations_post_city.reader(), quoted=True),
    primitives.restler_static_string(""",
            "locationId":"""),
    primitives.restler_static_string(_app_api_locations_post_locationId.reader(), quoted=False),
    primitives.restler_static_string(""",
            "postalCode":"""),
    primitives.restler_static_string(_app_api_locations_post_postalCode.reader(), quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/departments/update"
)
req_collection.add_request(request)

# Endpoint: /app/api/departments/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("departments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/departments/{id}"
)
req_collection.add_request(request)

# Endpoint: /app/api/employees, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/employees"
)
req_collection.add_request(request)

# Endpoint: /app/api/employees, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/employees"
)
req_collection.add_request(request)

# Endpoint: /app/api/employees, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/employees"
)
req_collection.add_request(request)

# Endpoint: /app/api/employees, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("employeeId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/employees"
)
req_collection.add_request(request)

# Endpoint: /app/api/employees, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/employees"
)
req_collection.add_request(request)

# Endpoint: /app/api/employees/data/department/{departmentId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("data"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("department"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/employees/data/department/{departmentId}"
)
req_collection.add_request(request)

# Endpoint: /app/api/employees/data/employee-project-data/{employeeId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("data"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employee-project-data"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/employees/data/employee-project-data/{employeeId}"
)
req_collection.add_request(request)

# Endpoint: /app/api/employees/data/manager-project-data/{employeeId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("data"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("manager-project-data"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/employees/data/manager-project-data/{employeeId}"
)
req_collection.add_request(request)

# Endpoint: /app/api/employees/delete, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("delete"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("employeeId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/employees/delete"
)
req_collection.add_request(request)

# Endpoint: /app/api/employees/save, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("save"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/employees/save"
)
req_collection.add_request(request)

# Endpoint: /app/api/employees/update, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("update"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/employees/update"
)
req_collection.add_request(request)

# Endpoint: /app/api/employees/username/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("username"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/employees/username/{username}"
)
req_collection.add_request(request)

# Endpoint: /app/api/employees/username/{username}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("username"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/employees/username/{username}"
)
req_collection.add_request(request)

# Endpoint: /app/api/employees/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("employees"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/employees/{id}"
)
req_collection.add_request(request)

# Endpoint: /app/api/locations, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/locations"
)
req_collection.add_request(request)

# Endpoint: /app/api/locations, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "adr":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "locationId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "postalCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_appapilocationspost,
            'dependencies':
            [
                _app_api_locations_post_adr.writer(),
                _app_api_locations_post_city.writer(),
                _app_api_locations_post_locationId.writer(),
                _app_api_locations_post_postalCode.writer()
            ]
        }

    },

],
requestId="/app/api/locations"
)
req_collection.add_request(request)

# Endpoint: /app/api/locations, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "adr":"""),
    primitives.restler_static_string(_app_api_locations_post_adr.reader(), quoted=True),
    primitives.restler_static_string(""",
    "city":"""),
    primitives.restler_static_string(_app_api_locations_post_city.reader(), quoted=True),
    primitives.restler_static_string(""",
    "locationId":"""),
    primitives.restler_static_string(_app_api_locations_post_locationId.reader(), quoted=False),
    primitives.restler_static_string(""",
    "postalCode":"""),
    primitives.restler_static_string(_app_api_locations_post_postalCode.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/locations"
)
req_collection.add_request(request)

# Endpoint: /app/api/locations, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("locationId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/locations"
)
req_collection.add_request(request)

# Endpoint: /app/api/locations, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/locations"
)
req_collection.add_request(request)

# Endpoint: /app/api/locations/delete, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("delete"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("locationId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/locations/delete"
)
req_collection.add_request(request)

# Endpoint: /app/api/locations/save, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("save"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "adr":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "locationId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "postalCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/locations/save"
)
req_collection.add_request(request)

# Endpoint: /app/api/locations/update, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("update"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "adr":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "locationId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "postalCode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/locations/update"
)
req_collection.add_request(request)

# Endpoint: /app/api/locations/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/locations/{id}"
)
req_collection.add_request(request)

# Endpoint: /app/api/projects, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/projects"
)
req_collection.add_request(request)

# Endpoint: /app/api/projects, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "endDate":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["dd-MM-yyyy"]),
    primitives.restler_static_string(""",
    "projectId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "startDate":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["dd-MM-yyyy"]),
    primitives.restler_static_string(""",
    "status":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_appapiprojectspost,
            'dependencies':
            [
                _app_api_projects_post_endDate.writer(),
                _app_api_projects_post_projectId.writer(),
                _app_api_projects_post_startDate.writer(),
                _app_api_projects_post_status.writer(),
                _app_api_projects_post_title.writer()
            ]
        }

    },

],
requestId="/app/api/projects"
)
req_collection.add_request(request)

# Endpoint: /app/api/projects, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "endDate":"""),
    primitives.restler_static_string(_app_api_projects_post_endDate.reader(), quoted=True),
    primitives.restler_static_string(""",
    "projectId":"""),
    primitives.restler_static_string(_app_api_projects_post_projectId.reader(), quoted=False),
    primitives.restler_static_string(""",
    "startDate":"""),
    primitives.restler_static_string(_app_api_projects_post_startDate.reader(), quoted=True),
    primitives.restler_static_string(""",
    "status":"""),
    primitives.restler_static_string(_app_api_projects_post_status.reader(), quoted=True),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_static_string(_app_api_projects_post_title.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_appapiprojectsput,
            'dependencies':
            [
                _app_api_projects_put_endDate.writer(),
                _app_api_projects_put_projectId.writer(),
                _app_api_projects_put_startDate.writer(),
                _app_api_projects_put_status.writer(),
                _app_api_projects_put_title.writer()
            ]
        }

    },

],
requestId="/app/api/projects"
)
req_collection.add_request(request)

# Endpoint: /app/api/projects, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("projectId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/projects"
)
req_collection.add_request(request)

# Endpoint: /app/api/projects, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/projects"
)
req_collection.add_request(request)

# Endpoint: /app/api/projects/delete, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("delete"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("projectId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/projects/delete"
)
req_collection.add_request(request)

# Endpoint: /app/api/projects/save, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("save"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "endDate":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["dd-MM-yyyy"]),
    primitives.restler_static_string(""",
    "projectId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "startDate":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["dd-MM-yyyy"]),
    primitives.restler_static_string(""",
    "status":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/projects/save"
)
req_collection.add_request(request)

# Endpoint: /app/api/projects/update, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("update"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "endDate":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["dd-MM-yyyy"]),
    primitives.restler_static_string(""",
    "projectId":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "startDate":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["dd-MM-yyyy"]),
    primitives.restler_static_string(""",
    "status":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/projects/update"
)
req_collection.add_request(request)

# Endpoint: /app/api/projects/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:50118\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/app/api/projects/{id}"
)
req_collection.add_request(request)
