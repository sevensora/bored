SELECT rating, title FROM movies JOIN ratings ON movie.id = ratings.movie_id WHERE year = 2010
order by title asc, rating desc;
