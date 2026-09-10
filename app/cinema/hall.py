"""Module for CinemaHall class."""

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    """Represents a cinema hall and its sessions."""

    def __init__(self, number: int) -> None:
        """Initialize the hall with its number.

        Args:
            number (int): The unique identifier for the hall.
        """
        self.number = number

    def movie_session(
        self,
        movie_name: str,
        customers: list[Customer],
        cleaning_staff: Cleaner,
    ) -> None:
        """Conduct a full movie session including start, viewing, and cleanup.

        Args:
            movie_name (str): The title of the movie.
            customers (list[Customer]): List of Customer instances in the hall.
            cleaning_staff (Cleaner): The Cleaner instance
            responsible for cleanup.
        """
        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie=movie_name)

        print(f'"{movie_name}" ended.')

        cleaning_staff.clean_hall(number=self.number)
