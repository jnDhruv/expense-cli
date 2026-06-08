import argparse
import functions

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='available commands',help="all commands", required=True, dest="command");

# ADD - ADD A NEW EXPENSE
add_parser = subparsers.add_parser('add', help='add a new expense')
add_parser.add_argument("--desc", "-d","--description", help="expense description")
add_parser.add_argument("--amount", "-am", help="amount spent", type=float)
add_parser.set_defaults(func=functions.add)

# DELETE - DELETE AN EXISTING EXPENSE
delete_parser = subparsers.add_parser('delete', help='delete an existing expense')
delete_parser.add_argument("id", help="ID of the expense to delete", type=int)
delete_parser.set_defaults(func=functions.delete)

# LIST - LIST ALL EXPENSES
list_parser = subparsers.add_parser('list', help='list all expenses')
list_parser.set_defaults(func=functions.viewList)

args = parser.parse_args()
args.func(args)