# Copyright (C) 2012 Christopher Kaster
# This file is part of pyDanbooru
#
# You should have received a copy of the GNU General Public License
# along with pyDanbooru. If not, see <http://www.gnu.org/licenses/>


class Image:

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, image):
        inst = cls()
        inst.url = image["file_url"]
        inst.width = image["width"]
        inst.height = image["height"]
        inst.rating = image["rating"]
        inst.score = image["score"]
        inst.md5 = image["md5"]
        inst.preview_url = image["preview_url"]
        inst.preview_width = image["preview_width"]
        inst.preview_height = image["preview_height"]
        inst.sample_url = image["sample_url"]
        inst.sample_width = image["sample_width"]
        inst.sample_height = image["sample_height"]
        inst.tags = image["tags"].split(' ')
        return inst

    @classmethod
    def from_etree(cls, image):
        inst = cls()
        inst.url = image.attrib["file_url"]
        inst.width = image.attrib["width"]
        inst.height = image.attrib["height"]
        inst.rating = image.attrib["rating"]
        inst.score = image.attrib["score"]
        inst.md5 = image.attrib["md5"]
        inst.preview_url = image.attrib["preview_url"]
        inst.preview_width = image.attrib["preview_width"]
        inst.preview_height = image.attrib["preview_height"]
        inst.sample_url = image.attrib["sample_url"]
        inst.sample_width = image.attrib["sample_width"]
        inst.sample_height = image.attrib["sample_height"]
        inst.tags = image.attrib["tags"].split(' ')
        return inst
