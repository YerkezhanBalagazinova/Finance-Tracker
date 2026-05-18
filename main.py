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

      choice=input("Select: ")
      if not choice.isdigit():
          choice=int(choice)

          if choice==1:
              year=int(input("Year: "))
              month=int(input("Month: "))
              month_sum(transactions, year, month)

          elif choice==2:
              year=int(input("Year: "))
              month=int(input("Month: "))
              breakdown=exp_bycat(transactions, year, month)
              for cat, amount in breakdown.items():
                print(f"{cat}: {amount}")

          elif choice==3:
              year=int(input("Year: "))
              month=int(input("Month: "))
              limits={"food": 500, "transport": 300, "entertainment": 200}
              result= overspending(transactions, year, month, limits)
              if result:
                 print("Overspending in:", result)
              else:
                 print("No overspending")

          elif choice==4:
             print("bye bye")
             break

          else:
              print("select a number from 1 to 4")
              continue
          
      
      
