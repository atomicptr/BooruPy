#!/usr/bin/python
from BooruPy.booru import BooruPy
import urllib
import os

tags = raw_input("Tags (seperate with space): ").split(' ')

booru_handler = BooruPy("provider.js")

i = 0

for p in booru_handler.provider_list:
    print("[{0}] {1}".format(i, p.name))
    i += 1

pid = raw_input("Provider-ID:[0] ")

if not pid:
    pid = 0

booru_provider = booru_handler.get_provider_by_id(int(pid))

path = raw_input("Path:[{0}-{1}/] ".format(booru_provider.shortname, "-".join(tags)))

if not path:
    path = "{0}-{1}/".format(booru_provider.shortname, "-".join(tags))

if not path[len(path)-1] is "/":
    path += "/"

if not os.path.exists(path):
    os.mkdir(path)

downloaded = 0

for i in booru_provider.get_images(tags):
    url = i.url
    file_name = "%s-%s[%s].%s" % (
        booru_provider.shortname,
        '-'.join(tags),
        i.md5,
        i.url.split('.')[-1])
    local_path = path + file_name
    urllib.urlretrieve(url, local_path)
    print("Downloaded %s" % (file_name))
    downloaded += 1
