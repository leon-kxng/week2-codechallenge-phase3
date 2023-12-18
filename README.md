# Restaurant Review System

Welcome to the Restaurant Review System, a Python project for creating and managing customer reviews for different restaurants!

## Overview

This project provides a straightforward and intuitive system for managing customer reviews of various restaurants. The system consists of three main classes: `Customer`, `Restaurant`, and `Review`. Users can add customers, restaurants, and reviews, and retrieve information such as customer details, restaurant details, and average star ratings.

## Features

- **Customer Management:** Create and manage customer profiles.
- **Restaurant Reviews:** Add and view reviews for specific restaurants.
- **Data Analysis:** Retrieve information about customers, restaurants, and average ratings.

## Classes

### Customer

The `Customer` class represents a customer who can add reviews for restaurants. It includes methods such as:

- `full_name()`: Returns the full name of the customer.
- `restaurants()`: Returns a list of restaurants the customer has reviewed.
- `add_review(restaurant, rating)`: Adds a review for a specified restaurant.

### Restaurant

The `Restaurant` class represents a restaurant that can be reviewed. It includes methods such as:

- `average_star_rating()`: Returns the average star rating based on reviews.
- `customers()`: Returns a list of customers who have reviewed the restaurant.

### Review

The `Review` class represents a review submitted by a customer for a specific restaurant. It includes methods such as:

- `customer()`: Returns the customer who submitted the review.
- `restaurant()`: Returns the restaurant that was reviewed.
- `rating()`: Returns the star rating given in the review.

## How to Use

1. Clone the repository:

    ```bash
    git clone git@github.com:leon-kxng/week2-codechallenge-phase3.git
    cd restaurant-review-system
    ```

2. Install dependencies:

    ```bash
    # Assuming you have Python installed
    # Install any required Python packages
    ```

3. Run the script:

    ```bash
    # Assuming your main script is named main.py
    python main.py
    ```

## Dependencies

- Python 3.11.6

## Contribution

If you'd like to contribute to this project, feel free to open an issue or submit a pull request.

## Author

This application was crafted by [Leon](https://github.com/Leon-kxng). You can find more of [my work](https://github.com/Leon-kxng) on GitHub.
