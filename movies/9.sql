SELECT DISTINCT name FROM people JOIN stars ON people.id = stars.person_id JOIN movies ON movies.id = stars.movie_id WHERE movies.year = 2004
order by people.birth asc;
