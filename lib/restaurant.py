class Restaurant:
    # A class variable to store all restaurants created
    all_restaurants = []

    def __init__(self, name):
        # Initialize a Restaurant instance with a name and an empty list of reviews
        self.name = name
        self.reviews = []

        # Add the new instance to the class variable list containing all restaurants
        Restaurant.all_restaurants.append(self)

    # Method to return the name of the restaurant
    # Note: This method will cause an issue because it has the same name as the attribute 'name'
    def name(self):
        return self.name

    # Method to return the list of reviews of the restaurant
    # Note: This method will cause an issue because it has the same name as the attribute 'reviews'
    def reviews(self):
        return self.reviews

    # Method to return a list of unique customers who have reviewed this restaurant
    def customers(self):
        # Use set comprehension to get unique customers and convert it back to a list
        return list({review.customer for review in self.reviews})

    # Class method to return all restaurants created
    @classmethod
    def all(cls):
        return cls.all_restaurants
    
    # Method to calculate and return the average star rating
    def average_star_rating(self):
        # Sum the ratings from all reviews
        total_ratings = sum(review.rating for review in self.reviews)
        # Count the number of reviews
        num_reviews = len(self.reviews)

        # Calculate the average rating if there are reviews, otherwise return 0
        if num_reviews > 0:
            return total_ratings / num_reviews
        else:
            return 0  # Return 0 if there are no reviews yet

