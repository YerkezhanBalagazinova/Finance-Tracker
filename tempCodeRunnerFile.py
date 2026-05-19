from tracker import FinanceTracker
from models import Income, Expense
from reports import month_exp, month_come, overspending

def setup():
    t=FinanceTracker()
    t.add_transaction(Income(1000,"2026-05-01"))
    t.add_transaction(Expense(150,"2026-05-02","food"))
    t.add_transaction(Expense(50,"2026-05-03","transport"))
    t.add_transaction(Expense(200,"2026-05-10","food"))
    t.add_transaction(Expense(100,"2026-05-15","entertainment"))
    return t

def test1():
    tr=setup()
    got=month_exp(tr,2026,5)
    assert got==150+50+200+100
    print("test1 pass")

def test2():
    tr=setup()
    got=month_come(tr,2026,5)
    assert got==1000
    print("test2 pass")

def test3():
    tr=setup()
    limits={"food":300,"transport":100,"entertainment":200}
    got=overspending(tr,2026,5,limits)
    assert "food" in got
    assert "transport" not in got
    assert "entertainment" not in got
    print("test3 pass")

def test4():
    tr=FinanceTracker()
    got1=month_exp(tr,2026,5)
    got2=month_come(tr,2026,5)
    assert got1==0 and got2==0
    print("test4 pass")

if __name__=="__main__":
    test1()
    test2()
    test3()
    test4()
    print("all tests passed")

    