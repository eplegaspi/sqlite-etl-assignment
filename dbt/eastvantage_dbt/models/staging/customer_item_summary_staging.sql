SELECT
    Customers.customer_id,
    Customers.age,
    Items.item_name,
    CAST(SUM(COALESCE(Orders.quantity, 0)) AS INTEGER) AS total_quantity
FROM {{ ref('sales_source') }} as Sales
JOIN {{ ref('customers_source') }} as Customers
     ON Customers.customer_id
     = Sales.customer_id
JOIN {{ ref('orders_source') }} as Orders
    ON Orders.sales_id
    = Sales.sales_id
JOIN {{ ref('items_source') }} as Items
    ON Items.item_id
    = Orders.item_id
WHERE Customers.age BETWEEN 18 AND 35
GROUP BY Customers.customer_id, Customers.age, Items.item_id, Items.item_name
HAVING SUM(COALESCE(Orders.quantity, 0)) > 0
ORDER BY Customers.customer_id, Customers.age, Items.item_name