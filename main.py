from csv_handler import initialize_csv
from add_handler import add_expense
from update_handler import update_expense
from remove_handler import remove_expense
from summary_handler import view_expenses_summary, view_expenses_summary_by_month
from budget_handler import initialize_budget_csv, set_budget

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    parser.add_argument("--add", nargs=3, metavar=("DESCRIPTION", "AMOUNT", "DATE"), help="Add an expense with description, amount, and date (DD/MM/YYYY)")
    parser.add_argument("--update", nargs=3, metavar=("ID", "DESCRIPTION", "AMOUNT"), help="Update an expense by ID")
    parser.add_argument("--view", action="store_true", help="View a summary of all expenses")
    parser.add_argument("--view-by-month", action="store_true", help="View a summary of expenses grouped by month")
    parser.add_argument("--remove", metavar="ID", help="Remove an expense by ID")
    parser.add_argument("--set-budget", nargs=2, metavar=("MONTH/YEAR", "AMOUNT"), help="Set a budget for a specific month (MM/YYYY)")
    args = parser.parse_args()

    initialize_csv()
    initialize_budget_csv()

    if args.add:
        description, amount, date = args.add
        add_expense(description, amount, date)
    elif args.update:
        expense_id, description, amount = args.update
        update_expense(expense_id, description, amount)
    elif args.view:
        view_expenses_summary()
    elif args.view_by_month:
        view_expenses_summary_by_month()
    elif args.remove:
        remove_expense(args.remove)
    elif args.set_budget:
        month_year, amount = args.set_budget
        set_budget(month_year, amount)