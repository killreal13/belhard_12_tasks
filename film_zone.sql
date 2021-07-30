CREATE DATABASE film_zone;
USE film_zone;

CREATE TABLE user_types (
	id VARCHAR(20) primary key,
    name VARCHAR(20) NOT NULL
);

INSERT INTO user_types(id, name)
VALUES
	("USER", "User"),
    ("ADMIN", "Administrator");

CREATE TABLE persons (
	id INT auto_increment,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    birthday datetime NOT NULL,
    primary key (id)
);

CREATE TABLE users (
	login VARCHAR(20) NOT NULL,
    password VARCHAR(45) NOT NULL,
    user_type_id VARCHAR(20) NOT NULL,
    person_id INT NOT NULL,
    constraint fk_users_users_type
		foreign key (user_type_id)
        references user_types(id)
        on delete cascade
        on update cascade,
    constraint fk_users_persons
		foreign key (person_id)
        references persons(id)
        on delete cascade
        on update cascade,
    primary key (login)
);

CREATE TABLE emails (
	id INT auto_increment,
    email VARCHAR(50) NOT NULL,
    user_login VARCHAR(50) NOT NULL,
    constraint fk_emails_users
		foreign key (user_login)
        references users(login)
        on delete cascade
        on update cascade,
    primary key(id)
);

CREATE TABLE genres (
	id VARCHAR(30) primary key,
    name VARCHAR(30) NOT NULL
);

INSERT INTO genres (id, name) 
VALUES
 ("ACTION", "Action");
 
INSERT INTO genres (id, name) 
VALUES
	("ADVENTURE", "Adventure");
    
INSERT INTO genres (id, name) 
VALUES
	("COMEDY", "Comedy");
    
INSERT INTO genres (id, name) 
VALUES
	("DRAMA", "Drama");
    
INSERT INTO genres (id, name) 
VALUES
	("CRIME", "Crime");
    
INSERT INTO genres (id, name) 
VALUES
	("SCI_FI", "Sci_fi");
    
INSERT INTO genres (id, name) 
VALUES
	("FANTASY", "Fantasy");
    
INSERT INTO genres (id, name) 
VALUES
	("MUSICAL", "Musical");
    
INSERT INTO genres (id, name) 
VALUES
	("WESTERN", "Western");
    
INSERT INTO genres (id, name) 
VALUES
	("POST_APOCALYPTIC", "Post-apocalyptic");
    
INSERT INTO genres (id, name) 
VALUES
	("WAR", "War");
    
INSERT INTO genres (id, name) 
VALUES
	("FAMILY", "Family film");
    
INSERT INTO genres (id, name) 
VALUES
	("LOVE", "Love story");
    
INSERT INTO genres (id, name) 
VALUES
	("CARTOON", "Cartoon");
    
INSERT INTO genres (id, name) 
VALUES
	("HORROR", "Horror");
    
INSERT INTO genres (id, name) 
VALUES
	("THRILLER", "Thriller");
    
INSERT INTO genres (id, name) 
VALUES
	("DOCUMENTARY", "Documentary");
    
CREATE TABLE films (
	id INT auto_increment,
    duration INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    release_date datetime NOT NULL,
    rating FLOAT NOT NULL,
    director_id INT NOT NULL,
    constraint fk_films_persons
		foreign key (director_id)
        references persons(id)
        on delete cascade
        on update cascade,
    primary key(id)
);

CREATE TABLE user_favorite_films (
	user_login VARCHAR(50) NOT NULL,
    film_id INT NOT NULL,
    constraint fk_user_favorite_films_users
		foreign key (user_login)
        references users (login)
        on delete cascade
        on update cascade,
	constraint fk_user_favorite_films_films
		foreign key (film_id)
        references films (id)
        on delete cascade
        on update cascade
);

CREATE TABLE film_genres (
	film_id INT NOT NULL,
    film_genre_id VARCHAR(30) NOT NULL,
    constraint fk_film_genres_films
		foreign key (film_id)
        references films(id)
        on delete cascade
        on update cascade,
	constraint fk_film_genres_genres
		foreign key (film_genre_id)
        references genres(id)
        on delete cascade
        on update cascade
);

CREATE TABLE characters (
	id INT auto_increment,
    name VARCHAR(15) NOT NULL,
    comment VARCHAR(150),
    film_id INT NOT NULL,
    constraint fk_characters_films
		foreign key (film_id)
        references films(id)
        on delete cascade
        on update cascade,
    primary key (id)
);

CREATE TABLE characters_actors (
	character_id INT NOT NULL,
    person_id INT NOT NULL,
    constraint fk_characters_actors_characters
		foreign key (character_id)
        references characters (id)
        on delete cascade
        on update cascade,
	constraint fk_characters_actors_persons
		foreign key (person_id)
        references persons (id)
        on delete cascade
        on update cascade
);

