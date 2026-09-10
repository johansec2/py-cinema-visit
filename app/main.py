"""Main module to orchestrate the cinema visit workflow."""

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    movie: str,
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
) -> None:
    """Simulate a full cinema visit including bar sales and movie session.

    Args:
        movie (str): The name of the movie to be shown.
        customers (list[dict[str, str]]): List of customer data
        with 'name' and 'food'.
        hall_number (int): The number of the cinema hall.
        cleaner (str): The name of the cleaner assigned to the hall.
    """
    # Create Customer instances from dictionary data
    customer_instances: list[Customer] = []
    for cust_data in customers:
        customer_instance = Customer(
            name=cust_data["name"],
            food=cust_data["food"]
        )
        customer_instances.append(customer_instance)

    # Create Cleaner instance
    cleaner_instance = Cleaner(name=cleaner)

    # 1. Cinema bar sells food to each customer
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # 2. Schedule and conduct the movie session (includes cleaning at the end)
    hall = CinemaHall(hall_number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
