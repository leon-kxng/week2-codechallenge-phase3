class Review:
    # A class variable to store all reviews created
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        # Initialize a Review instance with customer, restaurant, and rating
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

        # Add the review to the restaurant's and customer's list of reviews
        restaurant.reviews.append(self)
        customer.reviews.append(self)

        # Add the review to the class variable list containing all reviews
        Review.all_reviews.append(self)

    # Method to return the customer of the review
    def customer(self):
        return self.customer

    # Method to return the restaurant of the review
    def restaurant(self):
        return self.restaurant

    # Method to return the rating of the review
    def rating(self):
        return self.rating

    # Class method to return all reviews created
    @classmethod
    def all(cls):
        return cls.all_reviews

