# -*- coding: utf8 -*-

file = open('/home/jro/crontab_output2.txt')

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
            total = nodes[ip][3] + int(speed)
            # Find max speed
            if nodes[ip][2] < int(speed):
                maxSpeed = int(speed)
            else:
                maxSpeed = nodes[ip][2]
        else:
            freq = 1
            maxSpeed = int(speed)
            total = maxSpeed
        # get average speed based on frequency from sampling
        avgSpeed = total / freq
        # Set nodes[ip] = [frequency, average Speed, max Speed, total]
        nodes[ip] = [freq, avgSpeed, maxSpeed, total]

print(nodes)
