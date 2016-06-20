# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 09:23:38 2016

@author: jgarciamejia
"""

import numpy as np
from tabulate import tabulate
#print "Hello, World!"

#wordlist = ['test','a','hello','bye','Felicia']
#for i,j in enumerate(wordlist):
#    print i,j
    
#    if 0:
#        for i in xrange(6):
#           print i, wordlist[i]


"""
counter = 8

while counter <= 100:
    if counter % 3 == 0 and counter % 5 == 0:
        print "FizzBuzz"
    elif counter % 3 == 0: 
         print "Fizz"
    elif counter % 5 == 0:
        print "Buzz"
    else: 
        print counter
    counter += 2


for i in np.arange(8,101,2):
    if i % 3 == 0 and i % 5 == 0:
        print "FizzBuzz"
    elif i % 3 == 0: 
         print "Fizz"
    elif i % 5 == 0:
        print "Buzz"
    else: 
        print i
"""

####### DAY 2

# below demonstrates the importance of understanding binarity and how numbers are represented 

#g = 10
#while g != 5:
#    g -= 0.000001
#print g    


# instead do something like 
#==============================================================================
# g=10
# while abs(g - 5) > 0.0000001:
#     g -= 0.000001
# print g
#==============================================================================

# Tuple syntax

#t = (2,3,4)
#print t*2

##dir(v) tells us all the ways in which a list can be modified
# help(v) opens up the class description of what a list can do

#==============================================================================
# List comprehension is a lot faster 
#==============================================================================
# the num for num kind of says append to L the numbers in the range specified
#if they fulfill the given conditions
#L = [num for num in range(100) if (num % 7 == 0) or (num % 11 == 0)]
#print (len(L))

## Asteroid excericse. Turn the follwoing into list comprheension

# Let's find all the near-earth Asteroids with 0.8 < a < 1.2 and e < 0.5.
# Each element is (name, semi-major axis (AU), eccentricity, orbit class)
# source: http://ssd.jpl.nasa.gov/sbdb_query.cgi

Asteroids = [('Eros', 1.457916888347732, 0.2226769029627053, 'AMO'),
             ('Albert', 2.629584157344544, 0.551788195302116, 'AMO'),
             ('Alinda', 2.477642943521562, 0.5675993715753302, 'AMO'),
             ('Ganymed', 2.662242764279804, 0.5339300994578989, 'AMO'),
             ('Amor', 1.918987277620309, 0.4354863345648127, 'AMO'),
             ('Icarus', 1.077941311539208, 0.826950446001521, 'APO'),
             ('Betulia', 2.196489260519891, 0.4876246891992282, 'AMO'),
             ('Geographos', 1.245477192797457, 0.3355407124897842, 'APO'),
             ('Ivar', 1.862724540418448, 0.3968541470639658, 'AMO'),
             ('Toro', 1.367247622946547, 0.4358829575017499, 'APO'),
             ('Apollo', 1.470694262588244, 0.5598306817483757, 'APO'),
             ('Antinous', 2.258479598510079, 0.6070051516585434, 'APO'),
             ('Daedalus', 1.460912865705988, 0.6144629118218898, 'APO'),
             ('Cerberus', 1.079965807367047, 0.4668134997419173, 'APO'),
             ('Sisyphus', 1.893726635847921, 0.5383319204425762, 'APO'),
             ('Quetzalcoatl', 2.544270656955212, 0.5704591861565643, 'AMO'),
             ('Boreas', 2.271958775354725, 0.4499332278634067, 'AMO'),
             ('Cuyo', 2.150453953345012, 0.5041719257675564, 'AMO'),
             ('Anteros', 1.430262719980132, 0.2558054402785934, 'AMO'),
             ('Tezcatlipoca', 1.709753263222791, 0.3647772103513082, 'AMO'),
             ('Midas', 1.775954494579457, 0.6503697243919138, 'APO'),
             ('Baboquivari', 2.646202507670927, 0.5295611095751231, 'AMO'),
             ('Anza', 2.26415089613359, 0.5371603112900858, 'AMO'),
             ('Aten', 0.9668828078092987, 0.1827831025175614, 'ATE'),
             ('Bacchus', 1.078135348117527, 0.3495569270441645, 'APO'),
             ('Ra-Shalom', 0.8320425524852308, 0.4364726062545577, 'ATE'),
             ('Adonis', 1.874315684524321, 0.763949321566, 'APO'),
             ('Tantalus', 1.289997492877751, 0.2990853014998932, 'APO'),
             ('Aristaeus', 1.599511990737142, 0.5030618532252225, 'APO'),
             ('Oljato', 2.172056090036035, 0.7125729402616418, 'APO'),
             ('Pele', 2.291471988746353, 0.5115484924883255, 'AMO'),
             ('Hephaistos', 2.159619960333728, 0.8374146846143349, 'APO'),
             ('Orthos', 2.404988778495748, 0.6569133796135244, 'APO'),
             ('Hathor', 0.8442121506103012, 0.4498204013480316, 'ATE'),
             ('Beltrovata', 2.104690977122337, 0.413731105995413, 'AMO'),
             ('Seneca', 2.516402574514213, 0.5708728441169761, 'AMO'),
             ('Krok', 2.152545170235639, 0.4478259793515817, 'AMO'),
             ('Eger', 1.404478323548423, 0.3542971360331806, 'APO'),
             ('Florence', 1.768227407864309, 0.4227761019048867, 'AMO'),
             ('Nefertiti', 1.574493139339916, 0.283902719273878, 'AMO'),
             ('Phaethon', 1.271195939723604, 0.8898716672181355, 'APO'),
             ('Ul', 2.102493486378346, 0.3951143067760007, 'AMO'),
             ('Seleucus', 2.033331705805067, 0.4559159977082651, 'AMO'),
             ('McAuliffe', 1.878722427225527, 0.3691521497610656, 'AMO'),
             ('Syrinx', 2.469752836845105, 0.7441934504192601, 'APO'),
             ('Orpheus', 1.209727780883745, 0.3229034563257626, 'APO'),
             ('Khufu', 0.989473784873371, 0.468479627898914, 'ATE'),
             ('Verenia', 2.093231870619781, 0.4865133359612604, 'AMO'),
             ('"Don Quixote"', 4.221712367193639, 0.7130894892477316, 'AMO'),
             ('Mera', 1.644476057737928, 0.3201425983025733, 'AMO')]

orbit_class = {'AMO':'Amor', 'APO':'Apollo', 'ATE':'Aten'}


#==============================================================================
# L = []
# for data in Asteroids:
#     name, a, e, t = data
#     if abs(a - 1) < 0.2 and e < 0.5:
#         L.append(name)
# print(L)
#==============================================================================


#L = [num for num in range(100) if (num % 7 == 0) or (num % 11 == 0)]
#print (len(L))

near_Earth = [name for (name, a, e , t) in Asteroids if abs(a - 1) < 0.2 and e < 0.5]
print near_Earth

#L = [name[0] for name in Asteroids if abs(name[1] - 1) < 0.2 and name[2] < 0.5]

asteroid_dict = {name:(a,e,t) for (name, a, e,t ) in Asteroids}
print asteroid_dict

for name in sorted(asteroid_dict):
    print name, asteroid_dict[name][0], asteroid_dict[name][1], asteroid_dict[name][2]


#### CLASS EXCERCISES: HOME REPEATS
## Excercise No.1 again

#near_list = [name for name, a, e, t in Asteroids if abs(a - 1) < 0.2 and e < 0.5]

## Excercise No.2
#asteroid_dict2 = {name:(a, e, t) for (name, a, e, t) in Asteroids}


## Excercise No.3
# print list sorted alphabetically by Asteroid name 
for name in sorted(asteroid_dict):
    print name, asteroid_dict[name][0],asteroid_dict[name][1],asteroid_dict[name][2]

# the following code uses tabulate found in the Python documentation 
# print list sorted alphabetically by Asteroid name with nice alignment
sort_ast_lst = []
for name in sorted(asteroid_dict):
    sort_ast_lst.append([name, asteroid_dict[name][0],asteroid_dict[name][1],asteroid_dict[name][2]])
    
#print sort_ast_lst
print tabulate(sort_ast_lst, headers = ['Asteroid','Semi-major Axis','Eccentricity', 'Class Code'])

# print list sorted alphabetically by Asteroid name with Class name instead of class code
# Recall that orbit_class = {'AMO':'Amor', 'APO':'Apollo', 'ATE':'Aten'}
sort_ast_lst2 = []
for name in sorted(asteroid_dict):
    sort_ast_lst2.append([name, asteroid_dict[name][0],asteroid_dict[name][1],orbit_class[asteroid_dict[name][2]]])
print tabulate(sort_ast_lst2, headers = ['Asteroid','Semi-major Axis','Eccentricity', 'Class Name'])

#==============================================================================
# 
# for name in sorted(asteroid_dict):
#     if asteroid_dict[name][2] == 'AMO':
#         sort_ast_lst.append([name, asteroid_dict[name][0],asteroid_dict[name][1],orbit_class['AMO']])
#     elif asteroid_dict[name][2] == 'AMO':
#         
#     else:
#==============================================================================
 

# print list sorted by semi-major axis
# I obtained the code below from sorting how to documentation
semi_sort = sorted(Asteroids, key=lambda name:name[1])
print tabulate(semi_sort, headers = ['Asteroid','Semi-major Axis','Eccentricity', 'Class Code'])


##### DAY 4: FUNCTIONS
# Have a module with two functions:
# 1) Returns list of near-Earth Asteroids
# 2) Returns a dictionary of all Asteroids 
# Return a list of near-Earth asteroids and a dictionary of all asteroids

### Part 1 & 2

def near_Earth_func(Asteroids_list):
    """ Returns list of near-Earth Asteroids"""
    near_Earth = [name for (name, a, e , t) in Asteroids_list if abs(a - 1) < 0.2 and e < 0.5]
    return near_Earth

def Asteroid_dict_maker_1(Asteroids_list):
    """Returns a dictionary of all Asteroids """
    return {name:(a, e, t) for (name, a, e, t) in Asteroids}


### We can also use for loops instead of list comprehension

def Asteroid_dict_maker(Asteroids_list):
    """Returns a dictionary of all Asteroids """
    # make an empty dictionary
    asteroid_dictionary = {}
    # step through the list of asteroids 
    for asteroid_data in Asteroids_list:
        # assign the first elements of each tuple - namely the name of Asteroid- to become a key in our dictionary
        
        # assign to each name its a, e, t
    # return the dictionary
   
#==============================================================================
# Useful modules: astropy, pyfits, pandas
#==============================================================================

## homework: play aroudn with libraries, review Chris code and scikit
## put up semi-major axis vs eccentricity and color dots by class

















        


