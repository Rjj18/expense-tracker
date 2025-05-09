import csv
import os
from csv_handler import EXPENSES_FILE
from budget_handler import BUDGET_FILE

def is_within_budget(month_year, amount):
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        total_expenses = 0.0

        # Calculate total expenses for the given month/year
        if os.path.exists(EXPENSES_FILE):
            with open(EXPENSES_FILE, mode="r", newline="") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if row[3][3:] == month_year:  # Match the month/year
                        total_expenses += float(row[2])

        # Read the budget for the month
        budget = None
        if os.path.exists(BUDGET_FILE):
            with open(BUDGET_FILE, mode="r", newline="") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if row[0] == month_year:
                        budget = float(row[1])
                        break

        if budget is None:
            return True  # No budget set, so we are within budget

        return (total_expenses + amount) <= budget
    except ValueError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False