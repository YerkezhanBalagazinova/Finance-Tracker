def month_sumex(transactions, year, month):
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



