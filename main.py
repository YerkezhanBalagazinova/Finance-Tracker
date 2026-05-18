import json 
from tracker import FinanceTracker
from jsmanage import loadTrsns
from reports import month_sum, exp_bycat, overspending

def main():
    tracker=FinanceTracker()
    transactions=loadTrsns("transactions.json")  
    for t in transactions:
        tracker.add_transaction(t)

    while True:
        print("1)Monthly report")
        print("2)Breakdown by category")
        print("3)Overspending")
        print("4)Exit")
        choice=input("Select: ")
        if not choice.isdigit():
            print("enter number 1-4")
            continue
        choice=int(choice)

        if choice==1:
            y=int(input("Year: "))
            m=int(input("Month: "))
            month_sum(tracker,y,m)

        elif choice==2:
            y=int(input("Year: "))
            m=int(input("Month: "))
            br=exp_bycat(tracker,y,m)
            for cat,amount in br.items():
                print(f"{cat}: {amount}")

        elif choice==3:
            y=int(input("Year: "))
            m=int(input("Month: "))
            limits={"food":500,"transport":300,"entertainment":200}
            res=overspending(tracker,y,m,limits)
            if res:
                print("Overspending:",res)
            else:
                print("No overspending")

        elif choice==4:
            print("bye")
            break
        else:
            print("choose 1-4")

if __name__=="__main__":
    main()