import datetime
import json
import sys

months = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10: "October",
    11: "November",
    12: "December"
}

def load():
    try:
        with open('data.json', 'r') as data:
            return json.load(data)["expenses"]
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        sys.stderr.write("Error: Corrupt or invalid data.json")
        sys.exit(1)

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

def update(args):
    # args - id, [desc], [amount]
    expenses = load()

    if not expenses:
        print("No expenses added yet!")
        return
    
    if not args.desc and not args.amount:
        print("No update values specified!")
        sys.exit(1)

    for exp in expenses:
        if exp["id"] == args.id:
            #update it
            if args.desc:
                exp["desc"] = args.desc
                print(f"Updated expense description to {args.desc}")
            if args.amount:
                exp["amount"] = args.amount
                print(f"Updated expense amount to {args.amount}")
            save(expenses)
            break
    else:
        print("No such expense found!")

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
            save(expenses)
            break
    else:
        print("No such expense found!")
    
def viewList(args):
    # args - 
    expenses = load()
    if not expenses:
        print("No expenses added yet!")
        return
    print(f"{"ID":<10}"
    + f"{"Description":<30}"
    + f"{"Amount":<15}"
    + "Date")
    for exp in expenses:
        print(f"{exp["id"]:<10}"
        + f"{exp["desc"]:<30}"
        + f"{exp["amount"]:<15}"
        + f"{exp["day"]:02d}-{exp["month"]:02d}-{exp["year"]:04d}")

def summary(args):
    # args - [month]
    expenses = load()
    if not expenses:
        print("No expenses added yet!")
        return
    total = 0
    if args.month:
        if args.month not in months:
            print(f"{args.month} is not a valid month!")
            return
        
        total = sum([exp["amount"] for exp in expenses if exp["month"] == args.month])
        print(f"Total expenses for {months[args.month]}: {total}")
    else:
        total = sum([exp["amount"] for exp in expenses])
        print(f"Total expenses: {total}")
