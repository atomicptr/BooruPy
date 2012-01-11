# Copyright (C) 2012 Christopher Kaster
# This file is part of BooruPy
#
# You should have received a copy of the GNU General Public License
# along with BooruPy. If not, see <http://www.gnu.org/licenses/>
import json
from xml.etree import ElementTree
import urllib
from image import Image

class BaseProvider:

    def _get_URLopener(self):
        return urllib.FancyURLopener({}) # todo: add proxy support

    def _get_json(self, request_url):
        opener = self._get_URLopener()
        raw_json = opener.open(request_url)
        return json.load(raw_json)

    def _get_xml(self, request_url):
        opener = self._get_URLopener()
        raw_xml = opener.open(request_url).read()
        return ElementTree.XML(raw_xml)

class DanbooruProvider(BaseProvider):
    def __init__(self, provider_info):
        if provider_info:
            self.key = provider_info["key"]
            self.name = provider_info["name"]
            self.url = ''.join((provider_info["url"],
                    provider_info["json-query"]))
        else:
            pass # TODO: raise error

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
    
class GelbooruProvider(BaseProvider):
    def __init__(self, provider_info):
        if provider_info:
            self.key = provider_info["key"]
            self.name = provider_info["name"]
            self.url = ''.join((provider_info["url"],
                provider_info["xml-query"]))

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
                    '&pid=',
                    str(page)
            ]
            page += 1
            page_link = ''.join(sb) 
            images = self._get_xml(page_link)
            if len(images) < limit:
                ende = True
            yield images

    def get_images(self, tags):
        for images in self._request_images(tags):
            for i in images:
                yield Image.from_etree(i)

