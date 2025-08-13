# SQLite ETL Assignment – SQL & Pandas Solutions

## Overview
This project demonstrates two approaches to solving the same ETL problem from an SQLite database:

1. **Pure SQL solution** – uses a single query to aggregate results.
2. **Pandas solution** – loads tables into DataFrames, merges, filters, groups, and outputs results.

Both approaches:
- Filter customers aged **18–35** (inclusive).
- Sum quantities purchased per customer and item.
- Ignore items with a total quantity of 0 (or `NULL`).
- Output results to CSV with a `;` delimiter.
- Ensure `total_quantity` is an integer (no decimals).
- Order by `customer_id` then `item_name`.

---

## Problem Description
A company tracks customer purchases in four tables:
- `Customers(customer_id, age)`
- `Sales(sales_id, customer_id)`
- `Orders(sales_id, item_id, quantity)`
- `Items(item_id, item_name)`

The task:
- Find total quantities per item bought by customers aged 18–35.
- Include `customer_id`, `age`, `item_name`, and `total_quantity`.
- Exclude items where total quantity is 0.
- Write results to two CSV files: one from SQL, one from Pandas.

---

## File Structure
```
.
├── main.py                 # Contains both solutions
├── S30 ETL Assignment.db   # SQLite database file (not included in repo)
|── output_sql.csv          # Result from SQL approach
├── output_pandas.csv       # Result from Pandas approach
└── README.md               
└── requirements.txt        # Contains dependency
```

---
Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage
### Run the script
```bash
python main.py
```

The script will:
1. Read `S30 ETL Assignment.db` in the same directory.
2. Produce:
   - `output_sql.csv` – result from pure SQL approach.
   - `output_pandas.csv` – result from Pandas approach.
3. Print the number of rows written for each method.

---

## Output Format
Both CSV files will have:
```text
customer_id;age;item_name;total_quantity
1;23;Item A;2
1;23;Item B;1
...
```
- **Delimiter**: `;`
- **Order**: `customer_id` ascending, then `item_name` ascending
- **Data types**: `total_quantity` as integer
