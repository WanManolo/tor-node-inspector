# -*- coding: utf8 -*-

file = open('./config/sample.txt')

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
            # Find max speed
            if nodes[ip][2] < int(speed):
                maxSpeed = int(speed)
            else:
                maxSpeed = nodes[ip][2]
        else:
            freq = 1
            maxSpeed = int(speed)
        # get average speed based on frequency from sampling
        avgSpeed = int(speed) / freq
        # Set nodes[ip] = [frequency, average Speed, max Speed]
        nodes[ip] = [freq, avgSpeed, maxSpeed]

print(nodes)
