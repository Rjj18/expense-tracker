import csv
import os

BUDGET_FILE = "budget.csv"

def initialize_budget_csv():
    if not os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Month/Year", "Budget"])

def set_budget(month_year, amount):
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError("Budget amount cannot be negative.")

        budgets = {}

        # Read existing budgets
        if os.path.exists(BUDGET_FILE):
            with open(BUDGET_FILE, mode="r", newline="") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    budgets[row[0]] = float(row[1])

        # Update or add the budget for the given month/year
        budgets[month_year] = amount

        # Write updated budgets back to the file
        with open(BUDGET_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Month/Year", "Budget"])
            for month, budget in budgets.items():
                writer.writerow([month, budget])

        print(f"Budget for {month_year} set to {amount} successfully.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")