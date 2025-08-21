with Sales as (
    select *
    from sqlite_scan('S30 ETL Assignment.db', 'sales')
)

select * from Sales