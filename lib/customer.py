from review import Review 

class Customer:
    # A class variable to store all customers created
    all_customers = []

    def __init__(self, given_name, family_name):
        # Initialize a Customer instance with given and family names and an empty list of reviews
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []

        # Add the new instance to the class variable list containing all customers
        Customer.all_customers.append(self)

    # Method to return the given name of the customer
    # Note: This method will cause an issue because it has the same name as the attribute 'given_name'
    def given_name(self):
        return self.given_name

    # Method to return the family name of the customer
    # Note: This method will cause an issue because it has the same name as the attribute 'family_name'
    def family_name(self):
        return self.family_name

    # Method to return the full name of the customer
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    # Method to return a list of unique restaurants reviewed by this customer
    def restaurants(self):
        # Use set comprehension to get unique restaurants and convert it back to a list
        return list({review.restaurant for review in self.reviews})

    # Method to add a new review
    def add_review(self, restaurant, rating):
        # Create a new Review instance and append it to the customer's reviews
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)

    # Class method to return all customers created
    @classmethod
    def all(cls):
        return cls.all_customers
    
    # Method to return the number of reviews by the customer
    def num_reviews(self):
        return len(self.reviews)

    # Class method to find a customer by full name
    @classmethod
    def find_by_name(cls, name):
        # Loop through all customers to find a match by full name
        for customer in cls.all_customers:
            if customer.full_name().lower() == name.lower():
                return customer
        return None  # Return None if no match is found

    # Class method to find all customers by given name
    @classmethod
    def find_all_by_given_name(cls, name):
        # Return a list of customers whose given name matches the input name
        return [customer for customer in cls.all_customers if customer.given_name.lower() == name.lower()]

