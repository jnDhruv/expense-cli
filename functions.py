import datetime
import json

def load():
    try:
        with open('data.json', 'r') as data:
            return json.load(data)["expenses"]
    except FileNotFoundError:
        return []

def save(expenses):
    with open('data.json', 'w') as data:
        json.dump({"expenses":expenses}, data)

def add(args):
    # args - desc, amount
    expenses = load()

    newId = max([exp["id"] for exp in expenses], default=0) + 1
    currDate = datetime.datetime.now();
    newExp = {"id": newId, "desc": args.desc, "amount": args.amount, 
    "year": currDate.year, "month":currDate.month, "day":currDate.day};

    expenses.append(newExp)
    save(expenses)
    print(f"Added an expense of {newExp["amount"]} spent on {newExp["desc"]}")

def delete(args):
    # args - id
    expenses = load()

    if not expenses:
        print("No expenses added yet!")
        return
    
    for exp in expenses:
        if exp["id"] == args.id:
            expenses.remove(exp)
            print(f"Deleted the expense '{exp["desc"]}' of {exp["amount"]}")
            break
    else:
        print("No such expense found!")
    save(expenses)
    
def viewList(args):
    expenses = load()
    if not expenses:
        print("No expenses added yet!")
        return
    for exp in expenses:
        print(exp)
