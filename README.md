# Expense Tracker CLI

## Overview
The Expense Tracker CLI is a Python-based command-line application that helps you manage your expenses efficiently. With this tool, you can:

Project based on the suggestion of the site [RoadMap](https://roadmap.sh/projects/expense-tracker).

- Add, update, and remove expenses.
- View a summary of all expenses.
- View expenses grouped by month.
- Set a budget for each month.
- Get alerts when expenses exceed the monthly budget.

## Features
- **Add Expenses**: Add expenses with a description, amount, and date.
- **Update Expenses**: Modify existing expenses by their unique ID.
- **Remove Expenses**: Delete expenses by their unique ID.
- **View Summary**: Display all expenses in a tabular format.
- **Monthly Summary**: View total expenses grouped by month.
- **Set Budget**: Define a budget for each month.
- **Budget Alerts**: Get warnings when expenses exceed the monthly budget.

## Installation
1. Clone the repository or download the project files.
2. Ensure you have Python 3.7 or higher installed on your system.
3. Install any required dependencies (if applicable).

## Usage
Run the application using the command line:

```bash
python main.py [OPTIONS]
```

### Available Commands
- `--add "DESCRIPTION" AMOUNT "DATE"`  
  Add a new expense. Example:
  ```bash
  python main.py --add "Groceries" 50.75 "08/05/2025"
  ```

- `--update ID "DESCRIPTION" AMOUNT`  
  Update an existing expense by ID. Example:
  ```bash
  python main.py --update 1 "Rent" 1200.00
  ```

- `--remove ID`  
  Remove an expense by ID. Example:
  ```bash
  python main.py --remove 1
  ```

- `--view`  
  View a summary of all expenses. Example:
  ```bash
  python main.py --view
  ```

- `--view-by-month`  
  View a summary of expenses grouped by month. Example:
  ```bash
  python main.py --view-by-month
  ```

- `--set-budget "MONTH/YEAR" AMOUNT`  
  Set a budget for a specific month. Example:
  ```bash
  python main.py --set-budget "05/2025" 2000.00
  ```

## File Structure
- `main.py`: Entry point for the application.
- `add_handler.py`: Handles adding expenses.
- `update_handler.py`: Handles updating expenses.
- `remove_handler.py`: Handles removing expenses.
- `summary_handler.py`: Handles viewing expense summaries.
- `budget_handler.py`: Handles setting and managing budgets.
- `budget_checker.py`: Checks if expenses are within the budget.
- `csv_handler.py`: Manages CSV file operations.

## Example Workflow
1. Set a budget for the current month:
   ```bash
   python main.py --set-budget "05/2025" 2000.00
   ```
2. Add an expense:
   ```bash
   python main.py --add "Groceries" 150.00 "08/05/2025"
   ```
3. View all expenses:
   ```bash
   python main.py --view
   ```
4. Get a monthly summary:
   ```bash
   python main.py --view-by-month
   ```
5. Update an expense:
   ```bash
   python main.py --update 1 "Groceries" 200.00
   ```
6. Remove an expense:
   ```bash
   python main.py --remove 1
   ```

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Roger Aparecido Silva D

---
Enjoy tracking your expenses and staying on budget!
