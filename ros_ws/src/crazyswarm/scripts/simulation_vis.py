#!/usr/bin/env python

import csv
import numpy as np
from pycrazyswarm import *

Z = 1.0

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    # Read In Simulation Data
    position_data = []
    with open('drone_coords.csv', 'r') as f:
        readCSV = csv.reader(f, delimiter=',')
        for row in readCSV:
            data = list(map(float, row))
            position_data.append(data)

    allcfs.takeoff(targetHeight=Z, duration=1.0+Z)
    timeHelper.sleep(1.5+Z)
    for data in position_data:
        for i, cf in enumerate(allcfs.crazyflies):
            pos_x = data[i * 3]
            pos_y = data[(i * 3) + 1]
            pos_z = data[(i * 3) + 2]
            pos = np.array([pos_x, pos_y, pos_z])
            cf.goTo(pos, 0, 1.0)

        timeHelper.sleep(1.0)

    allcfs.land(targetHeight=0.02, duration=1.0+Z)
    timeHelper.sleep(1.0+Z)
