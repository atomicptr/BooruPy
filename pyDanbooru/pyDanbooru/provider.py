# Copyright (C) 2012 Christopher Kaster
# This file is part of pyDanbooru
#
# You should have received a copy of the GNU General Public License
# along with pyDanbooru. If not, see <http://www.gnu.org/licenses/>
import urllib
import json
from image import Image

class Provider:
	def __init__(self, provider_entry):
		if provider_entry:
                        self.key = provider_entry["key"]
			self.name = provider_entry["name"]
			self.url = provider_entry["url"]
			self.json_query = provider_entry["json-query"]
		else:
			# todo: error handling
			pass
	def get_request_url(self, tags, limit=0, page=0): # todo: add more filter options
		req_link = "tags="
		for t in tags:
			req_link += t + "+"	
		req_link = req_link[:-1] # remove last character ("+")
		if limit > 0:
			req_link += "&limit={0}".format(limit)
		if page > 0:
			req_link += "&page={0}".format(page)
		return self.url + self.json_query.format(req_link)
	def get_json(self, request_url):
		# todo: add proxy support
		opener = urllib.FancyURLopener({})
		return opener.open(request_url)
	def get_images(self, request_url):
		raw_json = self.get_json(request_url)
		images = json.load(raw_json)
		
		image_list = []
		
		for i in images:
			image_list.append(Image(i))

		return image_list
