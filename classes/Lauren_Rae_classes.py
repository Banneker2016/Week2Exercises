# June 21, 2016
# How to use classes in Python!

################################ EXAMPLE #######################################
# From https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-
# 			classes-and-object-oriented-programming/
class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance

# # You can define something as a class!
# lauren = Customer('Lauren C.', 3000)
# print lauren.balance
# # Then run the functions on it 
# lauren.withdraw(2)
# print lauren.balance
# lauren.deposit(1)
# print lauren.balance

################################# DEFINE #######################################

'''
Create an 'asteroid' class with properties:
	eccentricity, semimajor axis, orbit class 
Put in a function that allows you to change the eccentricity
Put in a function that allows you to add a rotation period property 

ex. Apollo.eccentricity will return <>
	Apollo.update_eccentricity will change that number
'''

class Asteroid(object):
    """An asteroid in space!!!! Thx NASA ;^*
    Asteroids have the following properties:

    Attributes:
        eccentricity: A float within [0,1) representing the orbital shape
        				(A circle has e = 0)
        				(A parabola has e = 1)
        semimajor_axis: A float representing the distance of the asteroid from the Sun
        orbit_class: A string denoting the orbital class of the asteroid
    """

    def __init__(self, eccentricity, semimajor_axis, orbit_class):
        """Return an Asteroid object with a defined eccentricity, semimajor_axis,
        and orbit_class. """
        self.eccentricity = eccentricity
        self.semimajor_axis = semimajor_axis
        self.orbit_class = orbit_class

    def update_eccentricity(self, new_eccentricity):
        """Change the defined eccentricity to a value *new_eccentricity*"""
        if new_eccentricity <= 0 or new_eccentricity > 1:
            raise RuntimeError('Invalid eccentricity value.')
        self.eccentricity = new_eccentricity
        return self.eccentricity

    def add_rotation_period(self, rotation_period):
        """Create a new attribute:
        	rotation_period: A float representing the time for the asteroid to 
        						complete an orbit.
        And define it to be *rotation_period*"""
        self.rotation_period = rotation_period
        return self.rotation_period