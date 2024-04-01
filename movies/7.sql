SELECT rating, title FROM movies JOIN ratings ON movie.id = ratings.movie_id WHERE year = 2010
ORDER BY title asc, rating desc;
