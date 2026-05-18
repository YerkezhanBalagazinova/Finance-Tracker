def month_exp(transactions, year, month):
    sumofexpenses=0

    for t in transactions: 
        if t["type"]=="expense":
            date_str=t["date"]
            parts=date_str.split('-') 
            trsn_year=int(parts[0])
            trsn_month=int(parts[1])

            if trsn_year==year and trsn_month==month:
                sumofexpenses+=t["amount"]
    
    return sumofexpenses

def month_come(transactions, year, month):
    sumofincomes=0

    for t in transactions: 
        if t["type"]=="income":
            date_str=t["date"]
            parts=date_str.split('-') 
            trsn_year=int(parts[0])
            trsn_month=int(parts[1])

            if trsn_year==year and trsn_month==month:
                sumofincomes+=t["amount"]
    
    return sumofincomes

def month_sum(transactions, year, month):
    expenses=month_exp(transactions, year,month)
    incomes=month_come(transactions, year,month)
    balance= incomes-expenses

    print("monthly report {year}-{month:02d}:")
    print("expenses:", expenses)
    print("incomes:", incomes)
    print("balance:", balance)

def exp_bycat(transactions,year,month):
    cat_dict={}

    for t in transactions:
        if t["type"] !="expense":
            continue
        
        date_str=t["date"]
        parts=date_str.split('-')
        trsn_year=int(parts[0])
        trsn_month=int(parts[1])

        if trsn_year!=year or trsn_month!=month:
            continue

        if t["type"]=="expense":
            cat=t["category"]
            amount=t["amount"]

            if cat in cat_dict:
                cat_dict[cat]+=amount
            else:
                cat_dict[cat]=amount

    return cat_dict

def overspending(transactions,year,month, cat_limit):
    brdw=exp_bycat(transactions,year,month)
    oversp=[]

    for cat in cat_limit:
        if cat in brdw and brdw[cat]>cat_limit[cat]:
            oversp.append(cat)
    
    return oversp