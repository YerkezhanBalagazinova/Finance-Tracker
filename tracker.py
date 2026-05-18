from models import Income, Expense


class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        income_total = 0
        expense_total = 0

        for transaction in self.transactions:
            if transaction.transaction_type.lower() == "income":
                income_total += transaction.amount
            else:
                expense_total += transaction.amount

        return income_total - expense_total

    def get_transactions_by_month(self, year, month):
        target = f"{year}-{month:02d}"

        return [
            transaction
            for transaction in self.transactions
            if transaction.date.startswith(target)
        ]

    def get_category_breakdown(self, year, month):
        breakdown = {}

        monthly_transactions = self.get_transactions_by_month(year, month)

        for transaction in monthly_transactions:
            if transaction.transaction_type.lower() == "expense":

                category = transaction.category

                if category not in breakdown:
                    breakdown[category] = 0

                breakdown[category] += transaction.amount

        return breakdown


#generator
def iter_transactions_by_month(transactions, year, month):
    target = f"{year}-{month:02d}"

    for transaction in transactions:
        if transaction.date.startswith(target):
            yield transaction


#Statistics
def calculate_statistics(transactions):

    expenses = [
        transaction.amount
        for transaction in transactions
        if transaction.transaction_type.lower() == "expense"
    ]

    if not expenses:
        return {
            "max_expense": 0,
            "average_expense": 0,
            "total_expenses": 0,
            "transaction_count": len(transactions)
        }

    return {
        "max_expense": max(expenses),
        "average_expense": sum(expenses) / len(expenses),
        "total_expenses": sum(expenses),
        "transaction_count": len(transactions)
    }