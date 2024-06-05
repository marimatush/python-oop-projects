"""
Manage flatmates.
"""

from .bill import Bill


class Flatmate:
    """
    Object to manage a flatmate person who lives in a flat
    and pays a share of the bill.
    """

    def __init__(self, name: str, days_in_house: int) -> None:
        self.name: str = name
        self.days_in_house: int = days_in_house

    def pays(self, bill: Bill, flatmate2: "Flatmate") -> float:
        """Amount that a flatmate has to pay for a period."""
        weight: float = self.days_in_house / (
            self.days_in_house + flatmate2.days_in_house
        )
        to_pay: float = bill.amount * weight

        return to_pay
