# 9-1
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

        self.number_served = 0 # 9-4
    
    def describe_restaurant(self):
        print(self.restaurant_name + " - " + self.cuisine_type)
    
    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")
    
    # 9-4
    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served = self.number_served + increment

restaurant = Restaurant("Michael's", "American")

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2
andrews = Restaurant("Andrew's", "Chinese")
liams = Restaurant("Liam's", "French")
dishas = Restaurant("Disha's", "Indian")

andrews.describe_restaurant()
liams.describe_restaurant()
dishas.describe_restaurant()

# 9-3
restaurant = Restaurant("McDonalds", "American")
print(restaurant.number_served)
restaurant.number_served = 1000000
print(restaurant.number_served)
restaurant.increment_number_served(500)
print(restaurant.number_served)