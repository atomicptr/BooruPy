# Copyright (C) 2012 Christopher Kaster
# This file is part of BooruPy
#
# You should have received a copy of the GNU General Public License
# along with BooruPy. If not, see <http://www.gnu.org/licenses/>
import json
from xml.etree import ElementTree
import urllib
from image import Image

class DanbooruProvider:
    def __init__(self, provider_info):
        if provider_info:
            self.key = provider_info["key"]
            self.name = provider_info["name"]
            self.url = provider_info["url"]
            self.query = provider_info["json-query"]
        else:
            pass # TODO: raise error
    def get_json(self, request_url):
        # todo: add proxy support
        opener = urllib.FancyURLopener({})
        return opener.open(request_url)
    def get_request_url(self, tags, limit=0, page=0):
        req_link = "tags="
        for t in tags:
            req_link += t + "+"	
        req_link = req_link[:-1] # remove last character ("+")
        if limit > 0:
            req_link += "&limit={0}".format(limit)
        if page > 0:
            req_link += "&page={0}".format(page)
        return self.url + self.query.format(req_link)
    def get_images(self, request_url):
        raw_json = self.get_json(request_url)
        images = json.load(raw_json)
		
        image_list = []
		
        for i in images:
            image_list.append(Image(i))

        return image_list
    
class GelbooruProvider:
    def __init__(self, provider_info):
        if provider_info:
            self.key = provider_info["key"]
            self.name = provider_info["name"]
            self.url = provider_info["url"]
            self.query = provider_info["xml-query"]
    def get_xml(self, request_url):
        # todo: add proxy support
        opener = urllib.FancyURLopener({})
        return opener.open(request_url).read()
    def get_request_url(self, tags, limit=0, page=0):
        req_link = "&tags="
        for t in tags:
            req_link += t + "+"
        req_link = req_link[:-1]
        if limit > 0:
            req_link += "&limit={0}".format(limit)
        if page > 0:
            req_link += "&pid={0}".format(page)
        return self.url + self.query.format(req_link)
    def get_images(self, request_url):
        raw_xml = self.get_xml(request_url)
        element = ElementTree.XML(raw_xml)

        element_list = []

        for e in element:
            element_list.append({
                    "file_url": e.attrib["file_url"],
                    "width" : e.attrib["width"],
                    "height" : e.attrib["height"],
                    "rating" : e.attrib["rating"],
                    "score" : e.attrib["score"],
                    "md5" : e.attrib["md5"],
                    "preview_url" : e.attrib["preview_url"],
                    "preview_width" : e.attrib["preview_width"],
                    "preview_height" : e.attrib["preview_height"],
                    "sample_url" : e.attrib["sample_url"],
                    "sample_width" : e.attrib["sample_width"],
                    "sample_height" : e.attrib["sample_height"],
                    "tags" : e.attrib["tags"],
                })

        image_list = []

        for e in element_list:
            image_list.append(Image(e))

        return image_list
