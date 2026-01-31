#
# Note:
# http://localhost:7000/inventory/services/all/3 should be started ('3' is a parameter, it can be anything)
#

import requests
import json

url = "http://localhost:7000/inventory/services";


# Creating the json request
headers = {'client-id': 'ankur', 'Content-Type': 'application/json', 'Accept': 'application/json'}
response = requests.get(url=url + "/all/3", headers=headers)

# Response status code
print("response code =" + str(response.status_code))

# JSON response
response_body = str(response.json())
print("response json = " + response_body)

# Pretty print
response_body_formatted = json.dumps(response.json(), indent=6)
print("response_body_formatted = "+response_body_formatted)

