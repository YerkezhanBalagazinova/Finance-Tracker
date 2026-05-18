from abc import ABC
class Transaction(ABC):
    def __init__(self,amount,date,transaction_type):
        self.amount=amount 
        self.date=date
        self.transaction_type=transaction_type
class Income(Transaction):
    def __init__(self, amount, date):
        super().__init__(amount,date,"income")
    def get_category(self):
        return "income"
class Expense(Transaction):
    def __init__(self, amount, date,category):
        super().__init__(amount,date,"expense")
        self.category=category
    def get_category(self):
        return self.category
class Category:
    def __init__(self,name,spend_limit):
        self.name=name
        self.spend_limit=spend_limit



