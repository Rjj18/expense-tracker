import csv
import os
from csv_handler import EXPENSES_FILE, get_next_id
from budget_handler import BUDGET_FILE, initialize_budget_csv, set_budget
from budget_checker import is_within_budget
from datetime import datetime

def add_expense(description, amount, date):
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        # Validate date format
        try:
            datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Date must be in the format DD/MM/YYYY.")

        expense_id = get_next_id()

        # Check if the expense exceeds the budget for the month
        month_year = date[3:]  # Extract MM/YYYY from DD/MM/YYYY
        if not is_within_budget(month_year, amount):
            print(f"Warning: Adding this expense exceeds the budget for {month_year}.")

        with open(EXPENSES_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([expense_id, description, amount, date])

        print(f"Expense added successfully with ID: {expense_id}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")