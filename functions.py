import datetime
import json
import sys
import csv

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
    newExp = {"id": newId, "desc": args.desc, "amount": args.amount, "category": args.category, 
    "year": currDate.year, "month":currDate.month, "day":currDate.day};

    expenses.append(newExp)
    save(expenses)
    print(f"Added an expense of {newExp["amount"]} spent on {newExp["desc"]} (category: {args.category})")

def update(args):
    # args - id, [desc] / [amount] / [category]
    expenses = load()

    if not expenses:
        print("No expenses added yet!")
        return
    
    if not args.desc and not args.amount and not args.category:
        print("No update values specified!")
        sys.exit(1)

    for exp in expenses:
        if exp["id"] == args.id:
            # update it
            if args.desc:
                exp["desc"] = args.desc
                print(f"Updated expense description to {args.desc}")
            if args.amount:
                exp["amount"] = args.amount
                print(f"Updated expense amount to {args.amount}")
            if args.category:
                exp["category"] = args.category
                print(f"Updated expense category to {args.category}")

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
    # args - [category]
    expenses = load()
    if not expenses:
        print("No expenses added yet!")
        return
    filtered = expenses
    if args.category:
        filtered = [exp for exp in filtered if exp["category"] == args.category]
        if not filtered:
            print("No expenses match the given category!")
            return

    tableHeader()
    for exp in filtered:
        tableRow(exp)

def summary(args):
    # args - [month] [category]
    expenses = load()
    if not expenses:
        print("No expenses added yet!")
        return
    total = 0
    filtered = expenses
    if args.month:
        filtered = [exp for exp in filtered if exp["month"] == args.month]
    if args.category:
        filtered = [exp for exp in filtered if exp["category"] == args.category]
    categ = {}
    for exp in filtered:
        if exp["category"] not in categ:
            categ[exp["category"]] = 0
        categ[exp["category"]] += exp["amount"]
        total += exp["amount"]

    if args.month and not filtered:
        print(f"No expense found for {months[args.month]}!")
        return
    if args.category and not categ:
        print(f"No matching expense of '{args.category}' found!")
        return
    for cat in categ:
        print(f"{cat}: {categ[cat]}")
    if args.month:
        print(f"Total expenses for {months[args.month]}: {total}")
    else:
        print(f"Total expenses: {total}")

def export(args):
    expenses = load()
    if not expenses:
        print("No expenses added yet!")
        return

    with open('export.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Description", "Amount", "Category", "Date"])
        for exp in expenses:
            writer.writerow([exp["id"], exp["desc"], exp["amount"], exp["category"], f"{exp["day"]}-{exp["month"]}-{exp["year"]}"])
    print("Successfully exported expenses to 'export.csv'!")

def tableHeader():
    print(f"{"ID":<10}"
    + f"{"Description":<30}"
    + f"{"Amount":<15}"
    + f"{"Category":<20}"
    + f"{"Date"}")

def tableRow(exp):
    print(f"{exp["id"]:<10}"
    + f"{exp["desc"]:<30}"
    + f"{exp["amount"]:<15}"
    + f"{exp["category"]:<20}"
    + f"{exp["day"]:02d}-{exp["month"]:02d}-{exp["year"]:04d}")
