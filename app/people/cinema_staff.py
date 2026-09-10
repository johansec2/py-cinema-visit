"""Module for Cleaner class."""


class Cleaner:
    """Represents a cinema cleaner."""

    def __init__(self, name: str) -> None:
        """Initialize cleaner with name.

        Args:
            name (str): The name of the cleaner.
        """
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """Print that the cleaner is cleaning a specific hall.

        Args:
            hall_number (int): The number of the hall to be cleaned.
        """
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
