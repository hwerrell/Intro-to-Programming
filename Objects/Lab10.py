class Restaurant:

    def __init__ (self, restaurant_name, cuisine_type, number_served=0):      #instantiate attributes for Restaurant class
        """initialize Restaurant attributes"""
        #save parameters as attributes
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number_served):
        self.number_served = increment_number_served + self.number_served

    def show_number_served(self):
        print(f"Number of customers served at {self.restaurant_name} - {self.number_served}")

class IceCreamStand(Restaurant):
    """Restaurant Type - Ice Cream Stand"""

    def __init__ (self, restaurant_name, cuisine_type, flavors, number_served=0):   #instantiate attributes for IceCreamStand class
        super().__init__(restaurant_name, cuisine_type, number_served)              #set IceCreamStand class attributes to Restaurant class' attributes.
        """initialize Ice Cream Stand attributes"""                                 
        #save flavor parameter as an attribute
        self.flavors = flavors

    def describe_flavors(self):
        print(", ".join(self.flavors))

#Create restaurants and add info
Henrys = Restaurant("Hungry Henry's", "Frozen Dinners")
Reids = Restaurant("Ravenous Reid's", "Sushi")
Annas = Restaurant("Anxious Anna's", "Beverages")

Chill = IceCreamStand("Chill Out", "Ice Cream", ["vanilla", "chocolate", "raspberry", "mint chocolate chip"])

#Output
Henrys.describe_restaurant()
Henrys.open_restaurant()

Henrys.describe_restaurant()
Reids.describe_restaurant()
Annas.describe_restaurant()
Chill.describe_restaurant()

Henrys.set_number_served(3)

print(Henrys.number_served)

Henrys.increment_number_served(82)

print(Henrys.number_served)

Chill.describe_flavors()

Reids.increment_number_served(122)
Reids.show_number_served()