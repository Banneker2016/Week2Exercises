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

# Make list of asteroids near Earth
#Aster_list = [name for (name, a, e, t) in Asteroids if abs(a - 1) < 0.2 and e < 0.5]
#print Aster_list

# Make list of Semimajor axis for Amor types
SMAxis_AMO = [a for (name, a, e, t) in Asteroids if t == 'AMO']

# Make list of ECCENTRICITY for Amor types
Ecc_AMO = [e for (name, a, e, t) in Asteroids if t == 'AMO']

'''************************************************************************** '''

# Make list of Semimajor axis for Apollo types
SMAxis_APO = [a for (name, a, e, t) in Asteroids if t == 'APO']

# Make list of ECCENTRICITY for Apollo types
Ecc_APO = [e for (name, a, e, t) in Asteroids if t == 'APO']

'''***************************************************************************'''
# Make list of Semimajor axis for Aten types
SMAxis_ATE = [a for (name, a, e, t) in Asteroids if t == 'ATE']

# Make list of ECCENTRICITY for Aten types
Ecc_ATE = [e for (name, a, e, t) in Asteroids if t == 'ATE']
'''****************************************************************************'''

# Importing matplotlib
import matplotlib.pyplot as plt

# Making the plot using Semimajor axis vs eccentricity
plt.plot(Ecc_AMO, SMAxis_AMO, 'ro', Ecc_APO, SMAxis_APO, 'bo', Ecc_ATE, SMAxis_ATE, 'go')

# X and Y axes ranges
plt.axis([0, 1, 0, 3])

# Label axes
plt.xlabel ('Eccentricity')
plt.ylabel ('Semi-major Axis')
plt.title ('Semi-major Axis vs Eccentricity')

# Show the graph
plt.show()

#asteroid_dict = {name:(a,e,t) for (name,a,e,t) in Asteroids}
#print asteroid_dict['Eros']