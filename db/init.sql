drop table if exists movies;
create table movies(
    id int,
    name text,
    genres text,
    primary key (id)
);

drop table if exists ratings;
create table ratings(
    user_id int,
    movie_id int,
    rating real,
    primary key (user_id, movie_id)
);

create index ratings_index on ratings(user_id, movie_id);

copy movies(id, name, genres)
from '/data/movies.csv' delimiter ',' csv header;

copy ratings(user_id, movie_id, rating)
from '/data/ratings.csv' delimiter ',' csv header;
