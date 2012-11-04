#!/usr/bin/python
# 
# Copyright 2010 Daniel Snider
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""A Facebook Graph query of your friends and available locations are printed.

Requirements: modify the variable access_token

An Access token can be aquired here: https://developers.facebook.com/tools/explorer
Further Facebook documentation at: http://developers.facebook.com/docs/api
"""

import sys
import httplib
from urlparse import urlparse
import json

access_token = "" # MUST BE MODIFIED
directory = "/me/friends?fields=id,name,location,picture&access_token=" + access_token 
domain = "graph.facebook.com"

conn = httplib.HTTPSConnection(domain, 443, timeout = 20) #connect to the site
conn.request("GET", directory) #send GET
r1 = conn.getresponse() #read response
page =  r1.read()

# Converting JSON to Python
result = json.loads(page)
data =  result['data']

# Print each person with a location
for person in data:
	if "location" in person:
		name = person["name"]
		loc = person["location"]["name"]
		pic = person["picture"]["data"]["url"]
		link = "www.facebook.com/profile.php?id=" + person["id"]
		if not loc == None:
				print name, "-", loc, link

sys.exit(0)