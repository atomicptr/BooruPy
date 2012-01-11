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
            self.url = ''.join(provider_info["url"] +
                    provider_info["json-query"])
        else:
            pass # TODO: raise error

    def _get_json(self, request_url):
        # todo: add proxy support
        opener = urllib.FancyURLopener({})
        raw_json = opener.open(request_url)
        return json.load(raw_json)

    def _request_images(self, tags):
        limit = 100
        page = 0

        ende = False
        while not ende:
            sb = [  self.url,
                    'tags=',
                    '+'.join(tags),
                    '&limit=',
                    str(limit),
                    '&page=',
                    str(page)
            ]
            page += 1
            page_link = ''.join(sb) 
            images = self._get_json(page_link)
            if len(images) < limit:
                ende = True
            yield images

    def get_images(self, tags):
        for images in self._request_images(tags):
            for i in images:
                yield Image.from_dict(i)
    
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

        image_list = []

        for e in element:
            image_list.append(Image.from_etree(e))

        return image_list
