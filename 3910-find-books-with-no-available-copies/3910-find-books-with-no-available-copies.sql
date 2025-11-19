# Write your MySQL query statement below

with borrowed as (
    select
    book_id,
    count(book_id) as current_borrowers
    from borrowing_records
    where return_date is NULL
    group by book_id
)

select 
l.book_id,
l.title,
l.author,
l.genre,
l.publication_year,
b.current_borrowers
from borrowed b left join library_books l
on b.book_id=l.book_id
where b.current_borrowers=l.total_copies
order by b.current_borrowers desc, l.title asc