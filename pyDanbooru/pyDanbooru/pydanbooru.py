# Copyright (C) 2012 Christopher Kaster
# This file is part of pyDanbooru
#
# You should have received a copy of the GNU General Public License
# along with pyDanbooru. If not, see <http://www.gnu.org/licenses/>
import json
from provider import Provider

class pyDanbooru:
	def __init__(self, provider_list):
		providers = json.load(open(provider_list))
		self.provider_list = []
		for p in providers:
			self.provider_list.append(Provider(p))
	def get_provider_by_id(self, provider_id):
		if isinstance(provider_id, int):
			return self.provider_list[provider_id]
	def get_provider_by_key(self, provider_key):
                for p in self.provider_list:
                        if p.key is provider_key:
                                return p
	
