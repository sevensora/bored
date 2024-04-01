SELECT title FROM people
JOIN movies ON stars.movie_id = movies.id
JOIN people ON start.person_id = people.id
JOIN ratings ON ratings.movie_id = movies.id
WHERE people.name = "Chadwick Boseman" ORDER BY rating DESC
LIMIT 5;

