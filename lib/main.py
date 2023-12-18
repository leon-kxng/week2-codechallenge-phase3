from customer import Customer
from restaurant import Restaurant
from review import Review

# Create customer instances
customer1 = Customer("Travis", "Scott")
customer2 = Customer("Kanye", "West")

# Define restaurant2 (assuming Restaurant takes a name as its argument)
restaurant2 = Restaurant("Example Restaurant Name")

# Create a review instance
review2 = Review(customer2, restaurant2, 5)

# Print customer, restaurant ratings, and number of reviews
print(f"Name: {customer1.full_name()}")
print(f"Rating: {restaurant2.average_star_rating()}")
print(f"Review: {customer2.num_reviews()}")

