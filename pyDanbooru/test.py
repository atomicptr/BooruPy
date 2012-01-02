from pyDanbooru.pydanbooru import pyDanbooru
import os
import urllib2

# configs

tags = raw_input("Tags (seperate with space): ").split(' ')

pydan = pyDanbooru("provider.js")

i = 0

for p in pydan.provider_list:
        print("{0}, {1}".format(i, p.name))
        i += 1

pid = raw_input("Provider-ID:[0] ")

if not pid:
        pid = 0

provider = pydan.get_provider_by_id(int(pid))

path = raw_input("Path:[{0}-{1}/] ".format(provider.key, "-".join(tags)))

if not path:
        path = "{0}-{1}/".format(provider.key, "-".join(tags))

if not path[len(path)-1] is "/":
        path += "/"

if not os.path.exists(path):
        os.mkdir(path)

file_count = raw_input("file download count:[10] ")

if not file_count:
        file_count = 10

print("download json filelist...")

images = provider.get_images(provider.get_request_url(tags, limit=file_count))

print("done")

filesize = 0.0

for i in images:
        filesize += i.filesize

downloaded = 0.0
last_fsd = 0.0

for i in images:
        file_name = i.url.split('/')[-1]
        u = urllib2.urlopen(i.url)
        f = open(path + file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print("Downloading: %s Bytes: %s" % (file_name, file_size))

        file_size_dl = 0
        last_fsd = 0
        block_sz = 8192
        while True:
                buffer = u.read(block_sz)
                if not buffer:
                        break
                file_size_dl += len(buffer)
                f.write(buffer)
                downloaded += file_size_dl - last_fsd
                last_fsd = file_size_dl
                status = r"%s [File: %3.2f%%] [All: %3.2f%%]" % (
                        file_size_dl,
                         file_size_dl * 100. / file_size,
                         downloaded * 100 / filesize)
                print(status)
        f.close()
