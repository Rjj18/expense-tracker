import csv
from csv_handler import EXPENSES_FILE

def update_expense(expense_id, description, amount):
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        expenses = []
        expense_found = False

        with open(EXPENSES_FILE, mode="r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0] == expense_id:
                    expenses.append([expense_id, description, amount, row[3]])  # Keep the original date
                    expense_found = True
                else:
                    expenses.append(row)

        if not expense_found:
            print(f"No expense found with ID: {expense_id}")
            return

        with open(EXPENSES_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(expenses)

        print(f"Expense with ID {expense_id} updated successfully.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")