# -*- coding: utf8 -*-
from collections import OrderedDict
#import os

# optional
# os.system("clear")

file = open('/mnt/d/Tor Browser/Browser/TorBrowser/Data/Tor/cached-microdesc-consensus')
# initial speed and hash
w = 0
nodes = {}
for line in file:
    line = line.rstrip()
    if line.startswith("r "):
        ip = line.split(' ')[5]
    if line.startswith("w "):
        w += 1
        nodes[ip] = int(line.replace("w Bandwidth=", '').split(' ')[0])

nodesBySpeed = OrderedDict(
    sorted(nodes.items(), key=lambda x: x[1], reverse=True))
n = 0
for ip in enumerate(nodesBySpeed):
    if n == 100:
        break
    print("{:20}".format(ip[1]), ':  ', nodes[ip[1]])
    n += 1

print("Existing nodes: ", w)
file.close()
