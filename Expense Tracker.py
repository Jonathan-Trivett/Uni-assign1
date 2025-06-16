import json

class Expense:
    def __init__(self, date, amount, description):
        self.date = date
        self.amount = amount
        self.description = description

    def to_dict(self):
        return {
            'date': self.date,
            'amount': self.amount,
            'description': self.description
        }

    @staticmethod
    def from_dict(data):
        return Expense(data['date'], data['amount'], data['description'])

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.expenses = []
        self.filename = filename
        self.load_expenses()

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            self.save_expenses()
            print("Expense removed successfully.")
        else:
            print("Invalid expense index.")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses recorded.")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. {expense.date} - £{expense.amount:.2f} - {expense.description}")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: £{total:.2f}")

    def save_expenses(self):
        with open(self.filename, 'w') as f:
            json.dump([expense.to_dict() for expense in self.expenses], f, indent=4)

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.expenses = [Expense.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []

if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                amount = float(input("Enter amount (£): "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            description = input("Enter description: ")
            expense = Expense(date, amount, description)
            tracker.add_expense(expense)
            print("Expense added successfully.")

        elif choice == '2':
            try:
                index = int(input("Enter the index of the expense to remove: ")) - 1
            except ValueError:
                print("Invalid index. Please enter a number.")
                continue
            tracker.remove_expense(index)

        elif choice == '3':
            tracker.view_expenses()

        elif choice == '4':
            tracker.total_expenses()

        elif choice == '5':
            print("Exiting Expense Tracker.")
            break

        else:
            print("Invalid choice. Please try again.")

