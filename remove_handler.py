import csv
from csv_handler import EXPENSES_FILE

def remove_expense(expense_id):
    try:
        expenses = []
        expense_found = False

        # Read all expenses and filter out the one to remove
        with open(EXPENSES_FILE, mode="r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header
            for row in reader:
                if row[0] == expense_id:
                    expense_found = True
                else:
                    expenses.append(row)

        if not expense_found:
            print(f"No expense found with ID: {expense_id}")
            return

        # Write updated expenses back to the file
        with open(EXPENSES_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)  # Write header
            writer.writerows(expenses)

        print(f"Expense with ID {expense_id} removed successfully.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")