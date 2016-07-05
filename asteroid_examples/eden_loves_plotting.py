#1) take asteroid listAMO':'Amor', 'APO':'Apollo', 'ATE':'Aten'
#2) plot semimajor axis v eccentricity
#3) color different points different colors corresponding to orbit classes
#4) push code into repository, specifically "plotting" subdirectory

import matplotlib.pyplot as plt
import numpy as np
from eden_loves_asteroids import astrolist

AMO_a = []
AMO_e = []

APO_a = []
APO_e = []

ATE_a = []
ATE_e = []

Asteroids = astrolist()

for t in Asteroids:
    if t[3] == 'AMO':
        AMO_a.append(t[1])
        AMO_e.append(t[2])
    elif t[3] == 'APO':
        APO_a.append(t[1])
        APO_e.append(t[2])
    elif t[3] == 'ATE':
        ATE_a.append(t[1])
        ATE_e.append(t[2])

A, = plt.plot(AMO_a, AMO_e, 'ro', label = 'AMO')
B, = plt.plot(APO_a, APO_e, 'bo', label = 'APO')
C, = plt.plot(ATE_a, ATE_e, 'go', label = 'ATE')

plt.title('Semi-major axis v. eccentricity by orbit class')
plt.xlabel('Semi-major axis (AU)')
plt.ylabel('Eccentricity')
plt.legend(loc='lower right', handles=[A, B, C])

plt.show()
