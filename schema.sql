-- Dropping tables in order if they exist to keep database consistent to project
DROP TABLE IF EXISTS media_has_character;
DROP TABLE IF EXISTS crossover;
DROP TABLE IF EXISTS has_background;
DROP TABLE IF EXISTS character_info;
DROP TABLE IF EXISTS media_character;
DROP TABLE IF EXISTS movie_actors;
DROP TABLE IF EXISTS movie;
DROP TABLE IF EXISTS anim_animators;
DROP TABLE IF EXISTS cgi_actors;
DROP TABLE IF EXISTS tv_show;
DROP TABLE IF EXISTS heard_in;
DROP TABLE IF EXISTS comic_artists;
DROP TABLE IF EXISTS comic;
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS song;
DROP TABLE IF EXISTS interacted_with;
DROP TABLE IF EXISTS users;


-- Creating tables for the database
CREATE TABLE users (
    username TEXT PRIMARY KEY,
    passwd TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone_no INT UNIQUE
);

CREATE TABLE song (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    s_title TEXT UNIQUE NOT NULL,
    year_no INT NOT NULL,
    favorite BOOLEAN DEFAULT 0,
    star_amount FLOAT(24) DEFAULT 0,
    media_comment TEXT,
    s_length FLOAT(24) NOT NULL,
    s_genre TEXT,
    s_singer TEXT
);

CREATE TABLE game (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    g_title TEXT UNIQUE NOT NULL,
    year_no INT NOT NULL,
    favorite BOOLEAN DEFAULT 0,
    media_comment TEXT,
    star_amount FLOAT(24) DEFAULT 0,
    g_genre TEXT
);

CREATE TABLE heard_in (
    s_id INT,
    g_id INT,
    FOREIGN KEY (s_id) REFERENCES song(id) ON DELETE CASCADE,
    FOREIGN KEY (g_id) REFERENCES game(id) ON DELETE CASCADE
);

CREATE TABLE comic (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    c_title TEXT UNIQUE NOT NULL,
    year_no INT NOT NULL,
    favorite BOOLEAN DEFAULT 0,
    star_amount FLOAT(24) DEFAULT 0,
    media_comment TEXT,
    c_series TEXT NOT NULL
);

CREATE TABLE comic_artists (
    c_id INT,
    c_artist TEXT NOT NULL,
    FOREIGN KEY (c_id) REFERENCES comic(id) ON DELETE CASCADE
);

CREATE TABLE tv_show (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tv_title TEXT UNIQUE NOT NULL,
    year_no INT NOT NULL,
    favorite BOOLEAN DEFAULT 0,
    star_amount FLOAT(24) DEFAULT 0,
    media_comment TEXT,
    tv_season_count INT NOT NULL,
    is_cgi BOOLEAN DEFAULT 0,
    is_animated BOOLEAN DEFAULT 0
);

CREATE TABLE cgi_actors (
    tv_id INT,
    cgi_actor TEXT NOT NULL,
    FOREIGN KEY (tv_id) REFERENCES tv_show(id) ON DELETE CASCADE
);

CREATE TABLE anim_animators (
    tv_id INT,
    anim_animator TEXT NOT NULL,
    FOREIGN KEY (tv_id) REFERENCES tv_show(id) ON DELETE CASCADE
);

CREATE TABLE movie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mo_title TEXT UNIQUE NOT NULL,
    year_no INT NOT NULL,
    favorite BOOLEAN DEFAULT 0,
    star_amount FLOAT(24) DEFAULT 0,
    media_comment TEXT,
    mo_director TEXT
);

CREATE TABLE movie_actors (
    mo_id INT,
    mo_actor TEXT NOT NULL,
    FOREIGN KEY (mo_id) REFERENCES movie(id) ON DELETE CASCADE
);

CREATE TABLE interacted_with (
    u_username TEXT NOT NULL,
    mo_id INT,
    c_id INT,
    s_id INT,
    g_id INT,
    tv_id INT,
    date_of_interaction TEXT NOT NULL,
    FOREIGN KEY (u_username) REFERENCES users(username) ON DELETE CASCADE,
    FOREIGN KEY (mo_id) REFERENCES movie(id) ON DELETE CASCADE,
    FOREIGN KEY (c_id) REFERENCES comic(id) ON DELETE CASCADE,
    FOREIGN KEY (s_id) REFERENCES song(id) ON DELETE CASCADE,
    FOREIGN KEY (g_id) REFERENCES game(id) ON DELETE CASCADE,
    FOREIGN KEY (tv_id) REFERENCES tv_show(id) ON DELETE CASCADE
);

CREATE TABLE media_character (
    ch_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ch_name TEXT UNIQUE NOT NULL,
    species TEXT NOT NULL,
    fur_color TEXT,
    eye_color TEXT,
    fluff_color TEXT NOT NULL
);

CREATE TABLE character_info (
    char_id INT,
    journal_entry TEXT,
    abilities TEXT NOT NULL,
    appearance TEXT,
    FOREIGN KEY (char_id) REFERENCES media_character(ch_id) ON DELETE CASCADE
);

CREATE TABLE has_background (
    char_id INT,
    ch_info_id INT,
    FOREIGN KEY (char_id) REFERENCES media_character(ch_id) ON DELETE CASCADE,
    FOREIGN KEY (ch_info_id) REFERENCES character_info(char_id) ON DELETE CASCADE
);

CREATE TABLE crossover (
    g_id INT,
    c_id INT,
    char_id INT,
    FOREIGN KEY (g_id) REFERENCES game(id) ON DELETE CASCADE,
    FOREIGN KEY (c_id) REFERENCES comic(id) ON DELETE CASCADE,
    FOREIGN KEY (char_id) REFERENCES media_character(ch_id) ON DELETE CASCADE
);

CREATE TABLE media_has_character (
    ch_id INT NOT NULL,
    g_id INT,
    c_id INT,
    tv_id INT,
    mo_id INT,
    s_id INT,
    FOREIGN KEY (ch_id) REFERENCES media_character(ch_id) ON DELETE CASCADE,
    FOREIGN KEY (g_id) REFERENCES game(id) ON DELETE CASCADE,
    FOREIGN KEY (c_id) REFERENCES comic(id) ON DELETE CASCADE,
    FOREIGN KEY (tv_id) REFERENCES tv_show(id) ON DELETE CASCADE,
    FOREIGN KEY (mo_id) REFERENCES movie(id) ON DELETE CASCADE,
    FOREIGN KEY (s_id) REFERENCES song(id) ON DELETE CASCADE
);


-- Insertion for initial table values
INSERT INTO users (username, passwd, email, phone_no)
VALUES
    ("sam_haj", "ilovecs2300", "sam@mst.edu", 3145551234);

INSERT INTO song (s_title, year_no , favorite, star_amount, media_comment, s_length, s_genre, s_singer)
VALUES 
   ("Undefeatable", 2022, true, 5, "This song is a banger", 4.24, "Rock", "Kellin Quinn"),
   ("Lights, Camera, Action!", 2017, true, 5, "Goes hard", 3.07, "Pop", "Sonic Force Soundtrack"),
   ("Fist Bump", 2017, false, 3, "It's alright", 4.27, "Rock", "Crush 40");

INSERT INTO game (g_title, year_no, favorite, media_comment, star_amount, g_genre)
VALUES 
   ("Sonic Forces", 2017, true, "Great game", 4.5, "3D Platformer"),
   ("Sonic Mania", 2017, true, "Best Sonic game", 5, "2D Platformer"),
   ("Sonic Heroes", 2003, false, "Not the best Sonic game", 3.5, "3D Mixed");

INSERT INTO comic (c_title, year_no, favorite, star_amount, media_comment, c_series)
VALUES
    ("Sonic the Hedgehog, Vol. 1: Fallout", 2018, false, 4.2, "Great start", "Arc 1"),
    ("Tangle and Whisper", 2019, true, 4.9, "Awesome characters", "Spinoff");

INSERT INTO tv_show (tv_title, year_no, favorite, star_amount, media_comment, tv_season_count, is_cgi, is_animated)
VALUES
    ("Sonic Boom", 2014, true, 4.5, "Funny show", 2, 0, 1),
    ("Sonic X", 2003, false, 3.8, "Nostalgic", 3, 0, 1),
    ("Knuckles", 2024, false, 3.2, "Alright", 1, 1, 0);

INSERT INTO movie (mo_title, year_no, favorite, star_amount, media_comment, mo_director)
VALUES
    ("Sonic the Hedgehog", 2020, true, 4.8, "Great adaptation", "Jeff Fowler"),
    ("Sonic the Hedgehog 2", 2022, true, 4.9, "Even better than the first", "Jeff Fowler"),
    ("Sonic the Hedgehog 3", 2024, false, 3.5, "Disappointing sequel", "Jeff Fowler");

INSERT INTO media_character (ch_name, species, fur_color, eye_color, fluff_color)
VALUES
    ("Sonic", "Hedgehog", "Blue", "Green", "Tan"),
    ("Tails", "Fox", "Orange", "Green", "White"),
    ("Knuckles", "Echidna", "Red", "Green", "White"),
    ("Amy Rose", "Hedgehog", "Pink", "Green", "Pink"),
    ("Shadow", "Hedgehog", "Black", "Red", "White");

INSERT INTO heard_in(s_id, g_id)
VALUES
    (2, 2);

INSERT INTO comic_artists(c_id, c_artist)
VALUES
    (1, "Ian Flynn"),
    (2, "Evan Stanley");

INSERT INTO cgi_actors(tv_id, cgi_actor)
VALUES
    (3, "Ben Schwartz"),
    (3, "Colleen O'Shaughnessey"),
    (3, "Idris Elba");

INSERT INTO anim_animators(tv_id, anim_animator)
VALUES
    (1, "Dee Bradley Baker"),
    (1, "Mike Pollock"),
    (2, "Jason Griffith"),
    (2, "Dan Green");

INSERT INTO movie_actors(mo_id, mo_actor)
VALUES
    (1, "Ben Schwartz"),
    (1, "James Marsden"),
    (2, "Jim Carrey"),
    (2, "Idris Elba"),
    (3, "Ben Schwartz"),
    (3, "James Marsden");

INSERT INTO interacted_with(u_username, mo_id, date_of_interaction)
VALUES
    ("sam_haj", 1, "2023-10-01"),
    ("sam_haj", 2, "2023-10-02"),
    ("sam_haj", 3, "2023-10-03");

INSERT INTO interacted_with(u_username, c_id, date_of_interaction)
VALUES
    ("sam_haj", 1, "2023-10-04"),
    ("sam_haj", 2, "2023-10-05");

INSERT INTO character_info(char_id, journal_entry, abilities, appearance)
VALUES
    (1, "I am the fastest thing alive!", "Super Speed", "Regular sized, blue downturned quills"),
    (2, "I am Sonic's best friend", "Flight", "Short, two tails, white fur tuft on chest"),
    (3, "I am the guardian of the Master Emerald", "Super Strength", "Muscular, red spiked quills"),
    (4, "I am Sonic's girlfriend", "Hammer Attack", "Short pink spikes, red dress"),
    (5, "I am the ultimate lifeform", "Chaos Control", "Red stripes on arms and quills");

INSERT INTO has_background(char_id, ch_info_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5);

INSERT INTO crossover(g_id, c_id, char_id)
VALUES
    (1, 1, 1),
    (2, 2, 2),
    (3, 1, 3),
    (1, 2, 4),
    (2, 3, 5);

INSERT INTO media_has_character(ch_id, g_id)
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 1),
    (3, 2),
    (3, 3),
    (4, 1),
    (4, 3),
    (5, 1),
    (5, 3);


