"""
Manage flatmates.
"""


class Flatmate:
    """
    Object to manage a flatmate person who lives in a flat
    and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        """Amount that a flatmate has to pay for a period."""
        pass
