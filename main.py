import json 
import re
from reports import month_exp, month_come, month_sum, exp_bycat,overspending

def loadtrns(filepath):
    try:
        with open(filepath, "r", encoding='utf-8') as f:
            data=json.load(f)
        return data
    except FileNotFoundError:
        print("Don't found the filee")
        return[]
    except json.JSONDecodeError:
        print("Error, format JSON")
    

def datacheck(datastr):
    if re.match(r'^\d{4}-\d{2}-\d{2}$', datastr):
       return True
    else:
       return False


def main():
    transactions = loadtrns("transaction.json")
    if not transactions:
        print("no data to work with ")

    while True:
      print("1)Monthly report")
      print("2)Breakdown by category")
      print("3)Overspending")
      print("4)Exit")

      choice = input("Select: ")
      if not choice.isdigit():
          print("select a number from 1 to 4")
          continue
      