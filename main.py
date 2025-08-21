import sqlite3
import pandas as pd
import csv

# ---------------------------
# Helpers
# ---------------------------
def write_csv_semicolon(rows, header, path):
    """Write rows to CSV with ';' as delimiter and without decimals."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(header)
        for r in rows:
            r = list(r)
            if len(r) >= 4 and isinstance(r[3], (float,)):
                r[3] = int(r[3])
            writer.writerow(r)

# ---------------------------
# Solution A: Pure SQL
# ---------------------------
def run_sql_solution(db_path, out_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    sql = """
    SELECT
        Customers.customer_id,
        Customers.age,
        Items.item_name,
        CAST(SUM(COALESCE(Orders.quantity, 0)) AS INTEGER) AS total_quantity
    FROM Sales
    JOIN Customers 
         ON Customers.customer_id
         = Sales.customer_id
    JOIN Orders 
        ON Orders.sales_id     
        = Sales.sales_id
    JOIN Items 
        ON Items.item_id
        = Orders.item_id
    WHERE Customers.age BETWEEN 18 AND 35
    GROUP BY Customers.customer_id, Customers.age, Items.item_id, Items.item_name
    HAVING SUM(COALESCE(Orders.quantity, 0)) > 0
    ORDER BY Customers.customer_id, Customers.age, Items.item_name
    """
    cur.execute(sql)
    rows = cur.fetchall()

    header = ["customer_id", "age", "item_name", "total_quantity"]
    write_csv_semicolon(rows, header, out_path)

    conn.close()
    return len(rows)

# ---------------------------
# Solution B: Pandas
# ---------------------------
def run_pandas_solution(db_path, out_path):
    with sqlite3.connect(db_path) as conn:
        customers = pd.read_sql_query("SELECT customer_id, age FROM Customers", conn)
        sales = pd.read_sql_query("SELECT sales_id, customer_id FROM Sales", conn)
        orders = pd.read_sql_query("SELECT sales_id, item_id, quantity FROM Orders", conn)
        items = pd.read_sql_query("SELECT item_id, item_name FROM Items", conn)

    out_df = (
        sales.merge(customers, on="customer_id")
        .merge(orders.assign(quantity=orders["quantity"].fillna(0)), on="sales_id")
        .merge(items, on="item_id")
        .query("18 <= age <= 35")
        .groupby(["customer_id", "age", "item_id", "item_name"], as_index=False)["quantity"].sum()
        .query("quantity > 0")
        .rename(columns={"quantity": "total_quantity"})
        .astype({"total_quantity": "int32"})
        .sort_values(["customer_id", "item_name"]))

    out_df[["customer_id", "age", "item_name", "total_quantity"]].to_csv(out_path, sep=";", index=False)
    return len(out_df)

db_file = "S30 ETL Assignment.db"
sql_output = "output_sql.csv"
pandas_output = "output_pandas.csv"

sql_rows = run_sql_solution(db_file, sql_output)
pd_rows  = run_pandas_solution(db_file, pandas_output)

print((sql_output, sql_rows, pandas_output, pd_rows))
