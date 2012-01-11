#!/usr/bin/python
from BooruPy.booru import BooruPy
import urllib2
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

#file_count = raw_input("file download count:[10] ")

#if not file_count:
#    file_count = 10

print("download image informations")

images = []
page_counter = 1
post_per_request = 100

while True:
    images += booru_provider.get_images(
        booru_provider.get_request_url(
            tags, limit=post_per_request, page=page_counter))
    page_counter += 1
    
    print("load new page {0}, {1}".format(len(images), page_counter))
    
    if (len(images) % post_per_request) > 0:
        break

print("done")

downloaded = 1

for i in images:
    file_name = "{0}.{1}".format(i.md5, i.url.split('.')[-1])
    u = urllib2.urlopen(i.url)
    f = open(path + file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print("Downloading: %s Bytes: %s" % (file_name, file_size))

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%s [File: %3.2f%%] [All: %s/%s]" % (
            file_size_dl,
            file_size_dl * 100. / file_size,
            downloaded,
            len(images))
        print(status)
    f.close()
    downloaded += 1
