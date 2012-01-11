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

path = raw_input("Path:[{0}-{1}/] ".format(booru_provider.key, "-".join(tags)))

if not path:
    path = "{0}-{1}/".format(booru_provider.key, "-".join(tags))

if not path[len(path)-1] is "/":
    path += "/"

if not os.path.exists(path):
    os.mkdir(path)

file_count = raw_input("file download count:[10] ")

if not file_count:
    file_count = 200

downloaded = 0

for i in booru_provider.get_images(tags):
    url = i.url
    file_name = url.split('/')[-1]
    local_path = path + file_name
    urllib.urlretrieve(url, local_path)
    downloaded += 1
