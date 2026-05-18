import json 
from models import Income,Expense
def file_action(function):
    def wrapper(*args,**kwargs):
        print("Working with file...")
        return function(*args,**kwargs)
    return wrapper
@file_action
def saveNewTrsns(transactions,file_path):
    data=[]
    for trsn in transactions:
        trsn_data={"type":trsn.transaction_type,"amount":trsn.amount,"date":trsn.date}
        if trsn.transaction_type=="expense":
            trsn_data["category"]=trsn.category
        data.append(trsn_data)
    with open(file_path,"w") as jsfl:
        json.dump(data,jsfl)

@file_action
def loadTrsns(file_path):
    transactions=[]
    try:
        with open(file_path,"r") as jsfl:
            data=json.load(jsfl)
        for item in data:
            if item["type"]=="income":
                transaction=Income(item["amount"],item["date"])
            else:
                transaction=Expense(item["amount"],item["date"],item["category"])
            transactions.append(transaction)
    except FileNotFoundError:
        print("File was not found")
    except json.JSONDecodeError:
        print("JSON file is broken")
    return transactions