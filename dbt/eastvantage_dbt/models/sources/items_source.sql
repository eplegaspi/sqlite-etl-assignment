with Items as (
    select *
    from sqlite_scan('S30 ETL Assignment.db', 'items')
)

select * from Items