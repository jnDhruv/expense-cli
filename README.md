# Expense Tracker CLI

A command-line application to manage personal expenses — add, update, delete, view, summarize, and export your spending data.

Built with Python using `argparse` for CLI handling and `json` for data persistence.

## Setup

```bash
git clone <your-repo-url>
cd expense-tracker
python app.py --help
```

No external dependencies. Uses Python standard library only.

## Usage

### Add an expense
```bash
python app.py add --desc "Lunch" --amount 20 --category food
```

### List all expenses
```bash
python app.py list
```

### Filter by category
```bash
python app.py list --category food
```

### Update an expense
```bash
python app.py update 1 --desc "Dinner" --amount 25
python app.py update 1 --category travel
```

### Delete an expense
```bash
python app.py delete 1
```

### Summary
```bash
python app.py summary                  # total + breakdown by category
python app.py summary --month 8        # filter by month
python app.py summary --category food  # filter by category
```

### Export to CSV
```bash
python app.py export
```
Exports all expenses to `export.csv` in the current directory.

## Data

Expenses are stored in `data.json` in the project root. Each expense contains:

| Field      | Type   | Description                  |
|------------|--------|------------------------------|
| id         | int    | Auto-incremented unique ID   |
| desc       | string | Expense description          |
| amount     | float  | Amount spent (must be > 0)   |
| category   | string | Expense category             |
| day        | int    | Day of creation              |
| month      | int    | Month of creation            |
| year       | int    | Year of creation             |
