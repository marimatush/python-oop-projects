"""
Manage bills.
"""


class Bill:
    """
    Object that contains data about a bill, such as
    total mount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
