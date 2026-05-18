def month_exp(tracker, year, month):
    sumofexpenses=0
    transactions=tracker.get_transactions_by_month(year,month)

    for t in transactions: 
        if t.transaction_type.lower()=="expense":
            sumofexpenses+=t.amount
    return sumofexpenses


def month_come(tracker, year, month):
    sumofincomes=0
    transactions=tracker.get_transactions_by_month(year,month)

    for t in transactions: 
        if t.transaction_type.lower()=="income":
            sumofincomes+=t.amount
    return sumofincomes



def month_sum(tracker, year, month):
    expenses=month_exp(tracker, year,month)
    incomes=month_come(tracker, year,month)
    balance= incomes-expenses

    print(f"monthly report {year}-{month:02d}:")
    print("expenses:", expenses)
    print("incomes:", incomes)
    print("balance:", balance)


def exp_bycat(tracker, year, month):
    return tracker.get_category_breakdown(year,month)



def overspending(tracker,year,month, cat_limit):
    brdw=tracker.get_category_breakdown(year,month)
    oversp=[]

    for cat in cat_limit:
        if cat in brdw and brdw[cat]>cat_limit[cat]:
            oversp.append(cat)
    return oversp
