# Copyright (C) 2012 Christopher Kaster
# This file is part of pyDanbooru
#
# You should have received a copy of the GNU General Public License
# along with pyDanbooru. If not, see <http://www.gnu.org/licenses/>
class Image:
    def __init__(self, image):
        try:
            self.url = image["file_url"]
            self.width = image["width"]
            self.height = image["height"]
            self.rating = image["rating"]
            self.score = image["score"]
            self.md5 = image["md5"]
            self.preview_url = image["preview_url"]
            self.preview_width = image["preview_width"]
            self.preview_height = image["preview_height"]
            self.sample_url = image["sample_url"]
            self.sample_width = image["sample_width"]
            self.sample_height = image["sample_height"]
            self.tags = image["tags"].split(' ')
        except:
            raise IOError("BooruPy: Something went wrong, no image recieved")
