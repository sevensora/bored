SELECT name FROM songs WHERE artist_ID = (SELECT id FROM artists WHERE name = "Post Malone");
