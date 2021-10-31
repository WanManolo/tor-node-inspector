# -*- coding: utf8 -*-

file = open('./config/sample.txt')

w = 0
nodes = {}
for line in file:
    # Skip sample breakline
    if "Existing nodes" not in line:
        # Extract IP
        ip = line.split(',')[0].strip().split('\'')[1].strip()
        # Extract bandwidth
        speed = line.split(',')[2].strip().split(')')[0]
        if ip in nodes:
            freq = nodes[ip][0] + 1
        else:
            freq = 1
        # get average speed based on frequency from sampling
        avgSpeed = int(speed) / freq
        nodes[ip] = [freq, avgSpeed]

print(nodes)
