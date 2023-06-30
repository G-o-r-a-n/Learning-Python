"""
Holiday Cost Calculator script.
This script will take input from a user and calculate the cost of a holiday.
"""

def hotel_cost(num_nights):
    """
    Calculate the total cost of the hotel stay.
    Args: 
        num_nights (int): The number of nights staying in the hotel.
    Returns:
        int: The total cost of the hotel stay.
    """
    cost = num_nights * 120
    return cost

def plane_cost(city_flight):
    """
    Calculate the cost of the flight depending on the destination city.
    Args:
        city_flight (str): The city to which the user will be flying.
    Returns:
        int: The cost of the flight.
    """
    if city_flight == "berlin":
        cost = 110
    elif city_flight == "lisbon":
        cost = 140
    elif city_flight == "madrid":
        cost = 120
    elif city_flight == "paris":
        cost = 100
    return cost

def car_rental_cost(rental_days):
    """
    Calculate the total cost of the car rental.
    Args:
        rental_days (int): The number of days the car will be rented.
    Returns:
        int: The total cost of the car rental.
    """
    cost = rental_days * 50
    return cost

def holiday_cost(hotel, plane, car_rental):
    """
    Calculate the total cost of the holiday.
    Args:
        hotel (int): The cost of the hotel stay.
        plane (int): The cost of the flight.
        car_rental (int): The cost of the car rental.
    Returns:
        int: The total cost of the holiday.
    """
    return hotel + plane + car_rental

# List of available cities.
cities = ["berlin", "lisbon", "madrid", "paris"]
# Display options to user.
print("\nCity break options: \n\nBerlin, \nLisbon, \nMadrid, \nParis.")
# Prompt user to choose destination.
city_flight = input("\nWhich city are you flying to? ").lower()
# Input validation for user's choice.
while city_flight not in cities:
    print("\nPlease enter one of the available city break options.")
    city_flight = input("\nWhich city are you flying to? ").lower()
# Prompts user to input number of nights for hotel stay.
num_nights = int(input("\nHow many nights will you be staying at a hotel? "))
# Prompts user to input number of days for car rental.
rental_days = int(input("\nHow many days will you be hiring a car for? "))

# Functions called to calculate various costs, stored in separate variables to
# later display a cost breakdown to user.
hotel = hotel_cost(num_nights)
plane = plane_cost(city_flight)
car_rental = car_rental_cost(rental_days)
total_cost = holiday_cost(hotel, plane, car_rental)
# Cost breakdown.
print(
    f"\nCity Break details:\n"
    f"\nFlight to {city_flight.capitalize()}: £{plane:.2f}"
    f"\nHotel for {num_nights} nights: £{hotel:.2f}"
    f"\nCar Rental for {rental_days} days: £{car_rental:.2f}"
    f"\nTotal Cost: £{total_cost:.2f}"
)
# End message.
print("\nThank you for using the Hyperion Holiday Calculator.")