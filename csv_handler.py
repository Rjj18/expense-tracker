import csv
import os

EXPENSES_FILE = "expenses.csv"

def initialize_csv():
    if not os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Description", "Amount", "Date"])

def get_next_id():
    try:
        with open(EXPENSES_FILE, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            ids = [int(row[0]) for row in reader]
            return max(ids) + 1 if ids else 1
    except FileNotFoundError:
        return 1
    except Exception as e:
        print(f"An unexpected error occurred while generating ID: {e}")
        return 1