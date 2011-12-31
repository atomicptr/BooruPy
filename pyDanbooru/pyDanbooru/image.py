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
			self.filesize = image["file_size"]
			self.rating = image["rating"]
			self.score = image["score"]
			self.md5 = image["md5"]
			self.sample_url = image["sample_url"]
			self.sample_width = image["sample_width"]
			self.sample_height = image["sample_height"]
			self.tags = image["tags"].split(' ')
		except:
			raise IOError("Something went wrong, no files found.")
