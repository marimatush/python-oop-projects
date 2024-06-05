"""
Manage PDF reports.
"""

from .flatmate import Flatmate
from .bill import Bill

from fpdf import FPDF


class PdfReport:
    """
    Object to manage a pdf file that contains data about
    the flatmates such as their names, their due amount
    and the period of the bill.
    """

    def __init__(self, filename: str) -> None:
        """
        Initialize a PdfReport object.

        Args:
            filename (str): The name of the pdf file to be generated.
        """
        if not filename.endswith(".pdf"):
            filename += ".pdf"
        self.filename = filename

    def generate(self, flatmate1: Flatmate, flatmate2: Flatmate, bill: Bill) -> None:
        """Generate a pdf report."""

        # Calculate the due amount of each flatmate
        flatmate1_pays: float = round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2)
        flatmate2_pays: float = round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2)

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add the title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", align="C", ln=1)

        # Add period lable and value
        pdf.set_font(family="Times", size=18, style="")
        pdf.cell(w=300, h=40, txt="Period")
        pdf.cell(w=150, h=40, txt=bill.period, ln=1)

        # Add the first flatmate's data
        pdf.cell(w=300, h=40, txt=f"{flatmate1.name} pays")
        pdf.cell(w=150, h=40, txt=str(flatmate1_pays), ln=1)

        # Add the second flatmate's data
        pdf.cell(w=300, h=40, txt=f"{flatmate2.name} pays")
        pdf.cell(w=150, h=40, txt=str(flatmate2_pays), ln=1)
        pdf.output(self.filename)
