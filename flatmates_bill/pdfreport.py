"""
Manage PDF reports.
"""


class PdfReport:
    """
    Object to manage a pdf file that contains data about
    the flatmates such as their names, their due amount
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2):
        """Generate a pdf report."""
        pass
