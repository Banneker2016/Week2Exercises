# Banneker Institute 2016 - June 20 - Lauren Chambers
# Plot asteroid semimajor axis vs. eccentricity, color coding different orbit classes
# Pushed into GitHub repository:
#           https://github.com/Banneker2016/Week2Exercises/tree/master/plotting

import "https://github.com/Banneker2016/Week2Exercises/blob/master/Lauren_asteroids.py" 
# Import functions and data defined in Lauren_asteroids.py
import matplotlib.pyplot as plt # Import matplotlib plotting module
import numpy as np # Import numeric python module

# Define array of asteroid data from Lauren_asteroids
# (Convert to numpy array for easy indexing)
asteroids = np.array(Lauren_asteroids.Asteroids) 

# Split up into lists of semimajor axes (a), eccentricities (e), and orbit classes (t)
a = asteroids[:, 1]
e = asteroids[:, 2]
t = asteroids[:, 3]

# Split up into 3 lists of (semimajor axis, eccentrity) for each different orbit class
# (Here, I'm defining three separate lists so I can easily make a plot legend later)
AMO = [[a, e] for name, a, e, t in asteroids if t == 'AMO']
APO = [(a, e) for name, a, e, t in asteroids if t == 'APO']
ATE = [(a, e) for name, a, e, t in asteroids if t == 'ATE']

# Create list of colors corresponding to each asteroid's orbital class
# (Another way of plotting with color, but doesn't allow for easy legend plotting)
# colors = []
# for orbit in t:
#       if orbit == "AMO":
#             colors.append('red')
#       if orbit == "APO":
#             colors.append('blue')
#       if orbit == "ATE":
#             colors.append('green')

# Finally, plot everything!
plt.scatter(*zip(*AMO), color='r', label= "AMO") # Not really sure how the * works...
plt.scatter(*zip(*ATE), color='b', label= "ATE") # But give each class a separate
plt.scatter(*zip(*APO), color='g', label= "APO") # label and color.
plt.legend()
plt.xlabel("Semimajor Axis (AU)")
plt.ylabel("Eccentricity")
plt.title("Asteroids by Orbital Class")
plt.show()