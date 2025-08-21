with Orders as (
    select *
    from sqlite_scan('S30 ETL Assignment.db', 'orders')
)

select * from Orders