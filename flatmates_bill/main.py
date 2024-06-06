from core.bill import Bill
from core.flatmate import Flatmate
from core.pdfreport import PdfReport


def get_bill_amount():
    # Get the bill amount and bill period from the user
    while True:
        try:
            bill_amount = float(input("Enter the bill amount: "))
            return bill_amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Function to get user input for flatmate data
def get_flatmate_data(name):
    while True:
        try:
            days_in_house = int(
                input(f"Enter the number of days {name} stayed in the house: ")
            )
            return days_in_house
        except ValueError:
            print("Invalid input. Please enter a valid number of days.")


if __name__ == "__main__":
    # Get the bill data
    bill_period: str = input("Enter the bill period: ")
    bill_amount = get_bill_amount()

    # Input first flatmate data
    flatmate1_name = input("\nEnter the name of the first flatmate: ")
    flatmate1_days_in_house = get_flatmate_data(flatmate1_name)

    # Input second flatmate data
    flatmate2_name = input("\nEnter the name of the second flatmate: ")
    flatmate2_days_in_house = get_flatmate_data(flatmate2_name)

    # Initialize objects
    the_bill = Bill(amount=bill_amount, period=bill_period)

    flatmate1 = Flatmate(name=flatmate1_name, days_in_house=flatmate1_days_in_house)
    flatmate2 = Flatmate(name=flatmate2_name, days_in_house=flatmate2_days_in_house)

    # Calculate due amount
    print(
        f"\n{flatmate1.name} pays: {flatmate1.pays(bill=the_bill, flatmate2=flatmate2)}"
    )
    print(
        f"{flatmate2.name} pays: {flatmate2.pays(bill=the_bill, flatmate2=flatmate1)}"
    )

    # Generate report
    pdf_report = PdfReport(filename=f"{the_bill.period}-report.pdf")
    pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
    print("\nAll righty! Here is your PDF report: Report.pdf")
