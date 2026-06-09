import argparse
import functions

def validateAmount(amt):
    try:
        amt = float(amt)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{amt} is not a valid amount!")
    if amt <= 0:
        raise argparse.ArgumentTypeError(f"Negative or zero amount entered!")
    return amt

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='available commands',help="all commands", required=True, dest="command");

# ADD - ADD A NEW EXPENSE
add_parser = subparsers.add_parser('add', help='add a new expense')
add_parser.add_argument("--desc", "-d","--description", help="expense description", required=True)
add_parser.add_argument("--amount", "-amt", help="amount spent", type=validateAmount, required=True)
add_parser.set_defaults(func=functions.add)

# DELETE - DELETE AN EXISTING EXPENSE
delete_parser = subparsers.add_parser('delete', help='delete an existing expense')
delete_parser.add_argument("id", help="ID of the expense to delete", type=int)
delete_parser.set_defaults(func=functions.delete)

# LIST - LIST ALL EXPENSES
list_parser = subparsers.add_parser('list', help='list all expenses')
list_parser.set_defaults(func=functions.viewList)

# SUMMARY - SUMMARIZE ALL EXPENSES
summary_parser = subparsers.add_parser('summary', help='summarize expenses')
summary_parser.add_argument("--month", "-m", help='summary of specified month', type=int)
summary_parser.set_defaults(func=functions.summary)

args = parser.parse_args()
args.func(args)