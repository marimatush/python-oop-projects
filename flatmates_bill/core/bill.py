"""
Manage bills.
"""


class Bill:
    """
    Object that contains data about a bill, such as
    total mount and period of the bill.
    """

    def __init__(self, amount: float, period: str) -> None:
        """
        Initialize a Bill object.
        Args:
            amount (float): The amount of the bill. Must be a positive number.
            period (str): The period of the bill.
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Bill amount should be positive.")
        self.amount: float = amount
        self.period: str = period
