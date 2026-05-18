import json 
import re
from reports import month_exp, month_come, month_sum, exp_bycat,overspending

def load_trns(filepath):
    try:
        with open(filepath, "r", encoding='utf-8') as f:
            data=json.load(f)
        return data
    except FileNotFoundError:
        print("Don't found the filee")
        return[]
    except json.JSONDecodeError:
        print("Error, format JSON")
    