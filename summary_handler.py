import csv
from csv_handler import EXPENSES_FILE
from collections import defaultdict

def view_expenses_summary():
    try:
        with open(EXPENSES_FILE, mode="r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header
            print(f"{'ID':<10}{'Description':<30}{'Amount':<10}{'Date':<15}")
            print("-" * 65)
            for row in reader:
                print(f"{row[0]:<10}{row[1]:<30}{row[2]:<10}{row[3]:<15}")
    except FileNotFoundError:
        print("No expenses found. The file does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def view_expenses_summary_by_month():
    try:
        expenses_by_month = defaultdict(float)

        with open(EXPENSES_FILE, mode="r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header
            for row in reader:
                date = row[3]  # Extract the date
                month_year = date[3:]  # Extract MM/YYYY from DD/MM/YYYY
                amount = float(row[2])
                expenses_by_month[month_year] += amount

        print(f"{'Month/Year':<15}{'Total Amount':<15}")
        print("-" * 30)
        for month_year, total in sorted(expenses_by_month.items()):
            print(f"{month_year:<15}{total:<15.2f}")
    except FileNotFoundError:
        print("No expenses found. The file does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")