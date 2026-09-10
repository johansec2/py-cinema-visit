"""Module for CinemaBar class."""

from app.people.customer import Customer


class CinemaBar:
    """Represents the cinema bar operations."""

    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        """Sell a product to a customer.

        Args:
            product (str): The name of the product being sold.
            customer (Customer): The customer instance buying the product.
        """
        print(f"Cinema bar sold {product} to {customer.name}.")
