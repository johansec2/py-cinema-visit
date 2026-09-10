"""Module for Customer class."""


class Customer:
    """Represents a cinema customer."""

    def __init__(self, name: str, food: str) -> None:
        """Initialize customer with name and desired food.

        Args:
            name (str): The name of the customer.
            food (str): The food item the customer wants to buy.
        """
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        """Print that the customer is watching a specific movie.

        Args:
            movie (str): The name of the movie being watched.
        """
        print(f'{self.name} is watching "{movie}".')