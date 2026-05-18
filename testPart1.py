from models import Income,Expense,Category
from jsmanage import saveNewTrsns,loadTrsns
income1=Income(1000,"2025-05-01")
assert income1.amount==1000
assert income1.date=="2025-05-01"
assert income1.transaction_type=="income"
expense1=Expense(200,"2026-03-10","food")
assert expense1.amount==200
assert expense1.date=="2026-03-10"
assert expense1.category=="food"
assert expense1.transaction_type=="expense"
transactions=loadTrsns("transactions.json")
assert len(transactions)>0
saveNewTrsns(transactions,"test.json")
newload=loadTrsns("test.json")
assert len(newload)==len(transactions)