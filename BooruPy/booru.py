# Copyright (C) 2012 Christopher Kaster
# This file is part of BooruPy
#
# You should have received a copy of the GNU General Public License
# along with BooruPy. If not, see <http://www.gnu.org/licenses/>
import json
from provider import DanbooruProvider, GelbooruProvider


class BooruManager:

    def __init__(self, providerlist_path, filter_nsfw=True):
        providers = json.load(open(providerlist_path))
        self.provider_list = []
        for p in providers:
            if p["type"] == "danbooru":
                self.provider_list.append(DanbooruProvider(p['url'], p['name'],
                    p['key'], filter_nsfw))
            elif p["type"] == "gelbooru":
                self.provider_list.append(GelbooruProvider(p['url'], p['name'],
                    p['key'], filter_nsfw))
            else:
                print("Unknown provider type: {0}".format(p["type"]))

    def get_provider_by_id(self, provider_id):
        if isinstance(provider_id, int):
            return self.provider_list[provider_id]

    def get_provider_by_key(self, provider_key):
        for p in self.provider_list:
            if p.key is provider_key:
                return p
