"""
Tests for flatmates bill app.
"""

import unittest
import uuid
import os

from flatmates_bill.bill import Bill
from flatmates_bill.flatmate import Flatmate
from flatmates_bill.pdfreport import PdfReport


class TestBill(unittest.TestCase):
    """Test Bill class."""

    def test_bill_creation(self):
        """Testing creating a bill object."""
        bill_amt = 120
        bill_period = "January 2024"

        new_bill = Bill(bill_amt, bill_period)
        self.assertEqual(new_bill.amount, bill_amt)
        self.assertEqual(new_bill.period, bill_period)

    def test_bill_creation_with_negative_amount(self):
        """Testing creating a bill object with negative amounmt"""
        bill_amt = -100
        bill_period = "February 2024"

        new_bill = Bill(amount=bill_amt, period=bill_period)
        self.assertEqual(new_bill.amount, bill_amt)
        self.assertEqual(new_bill.period, bill_period)


class TestFlatmate(unittest.TestCase):
    """Test Flatmate class."""

    def test_flatmate_creation(self):
        """Testing creating a new flatmate."""
        name = "Ann"
        days = 30

        new_flatmate = Flatmate(name=name, days_in_house=days)
        self.assertEqual(new_flatmate.name, name)
        self.assertEqual(new_flatmate.days_in_house, days)

    def test_flatmate_pays(self):
        """Testing paying amount of a flatmate for a period of time."""
        april_bill = Bill(amount=100, period="April 2024")
        flatmate_john = Flatmate(name="John", days_in_house=20)
        flatmate_ann = Flatmate(name="Ann", days_in_house=30)

        self.assertEqual(flatmate_john.pays(april_bill, flatmate_ann), 40)
        self.assertEqual(flatmate_ann.pays(april_bill, flatmate_john), 60)


class TestPdfReport(unittest.TestCase):
    """Test PdfReport class."""

    def test_creating_pdf_report_object(self):
        """Testing creating a new pdf report object."""
        filename = str(uuid.uuid4())

        pdf_report = PdfReport(filename=filename)
        self.assertEqual(pdf_report.filename, filename)

    def test_generating_pdf_report(self):
        """Testing generating a new pdf report."""
        june_bill = Bill(amount=300, period="June 2024")  # noqa
        flatmate1 = Flatmate(name="Marry", days_in_house=10)
        flatmate2 = Flatmate(name="Cara", days_in_house=20)
        filename = str(uuid.uuid4())

        pdf_report = PdfReport(filename=filename)
        pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2)
        self.assertTrue(os.path.exists(filename))


if __name__ == "__main__":
    unittest.main()