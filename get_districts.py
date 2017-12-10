#!/usr/bin/env python3

import json
import requests
import lxml.html
from collections import defaultdict

response = requests.get("http://tax1.co.monmouth.nj.us/cgi-bin/prc6.cgi?&ms_user=monm&passwd=data")
doc = lxml.html.fromstring(response.content)
counties = {x.text: x.get('value') for x in doc.cssselect('select[name="select_cc"] option')}

districts = defaultdict(dict)
for county_name, county_id in counties.items():
    response = requests.get(f"http://tax1.co.monmouth.nj.us/cgi-bin/prc6.cgi?&ms_user=monm&passwd=data&district={county_id}")
    doc = lxml.html.fromstring(response.content)
    for x in doc.cssselect('select[name="district"] option'):
        district_name = x.text
        district_id = x.get('value')
        if district_name in districts[county_name]:
            raise Exception(f"{district_name} is already in districts. name collision")
        else:
            districts[county_name][district_name] = district_id

with open('counties.json', 'w') as f:
    json.dump(counties, f, indent=4)

with open('districts.json', 'w') as f:
    json.dump(districts, f, indent=4)
