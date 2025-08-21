with Customers as (
    select *
    from sqlite_scan('S30 ETL Assignment.db', 'customers')
)

select * from Customers