select
    library_books.book_id,
    library_books.title,
    library_books.author,
    library_books.genre,
    library_books.publication_year,
    temp.current_borrowers
from library_books
join (
    select
        book_id,
        count(*) as current_borrowers
    from borrowing_records
    where return_date is null
    group by book_id
) temp
on library_books.book_id = temp.book_id
where library_books.total_copies = temp.current_borrowers
order by temp.current_borrowers desc, library_books.title asc