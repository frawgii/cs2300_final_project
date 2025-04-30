-- Dropping tables in order if they exist to keep database consistent to project
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS character_appearances;
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
DROP TABLE IF EXISTS game_genres;
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS song_singers;
DROP TABLE IF EXISTS song;
DROP TABLE IF EXISTS interacted_with;
DROP TABLE IF EXISTS users;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

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
    s_genre TEXT
);

CREATE TABLE song_singers (
    song_title TEXT,
    s_singer TEXT NOT NULL,
    FOREIGN KEY (song_title) REFERENCES song(s_title)
);

CREATE TABLE game (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    g_title TEXT UNIQUE NOT NULL,
    year_no INT NOT NULL,
    favorite BOOLEAN DEFAULT 0,
    media_comment TEXT,
    star_amount FLOAT(24) DEFAULT 0
);

CREATE TABLE heard_in (
    song_title TEXT,
    game_title TEXT,
    FOREIGN KEY (song_title) REFERENCES song(s_title),
    FOREIGN KEY (game_title) REFERENCES game(g_title)
);

CREATE TABLE game_genres (
    game_title TEXT,
    g_genre TEXT NOT NULL,
    FOREIGN KEY (game_title) REFERENCES game(g_title)
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
    comic_title TEXT,
    c_artist TEXT NOT NULL,
    FOREIGN KEY (comic_title) REFERENCES comic(c_title)
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
    cgi_title TEXT,
    cgi_actor TEXT NOT NULL,
    FOREIGN KEY (cgi_title) REFERENCES tv_show(tv_title)
);

CREATE TABLE anim_animators (
    anim_title TEXT,
    anim_animator TEXT NOT NULL,
    FOREIGN KEY (anim_title) REFERENCES tv_show(tv_title)
);

CREATE TABLE movie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mo_title TEXT UNIQUE NOT NULL,
    year_no INT NOT NULL,
    favorite BOOLEAN DEFAULT 0,
    star_amount FLOAT(24) DEFAULT 0,
    media_comment TEXT,
    mo_director TEXT,
    FOREIGN KEY (mo_title) REFERENCES media(title)
);

CREATE TABLE movie_actors (
    mo_title TEXT,
    mo_actor TEXT NOT NULL,
    FOREIGN KEY (mo_title) REFERENCES movie(mo_title)
);

CREATE TABLE interacted_with (
    u_username TEXT NOT NULL,
    movie_title TEXT,
    comic_title TEXT,
    song_title TEXT,
    tv_title TEXT,
    game_title TEXT,
    FOREIGN KEY (u_username) REFERENCES users(username),
    FOREIGN KEY (movie_title) REFERENCES movie(mo_title),
    FOREIGN KEY (comic_title) REFERENCES comic(c_title),
    FOREIGN KEY (song_title) REFERENCES song(s_title),
    FOREIGN KEY (tv_title) REFERENCES tv_show(tv_title),
    FOREIGN KEY (game_title) REFERENCES game(g_title)
);

CREATE TABLE media_character (
    ch_name TEXT PRIMARY KEY,
    species TEXT NOT NULL,
    skin_color TEXT,
    eye_color TEXT,
    fur_color TEXT NOT NULL
);

CREATE TABLE character_info (
    char_name TEXT,
    journal_entry TEXT,
    abilities TEXT NOT NULL,
    FOREIGN KEY (char_name) REFERENCES media_character(ch_name)
);

CREATE TABLE character_appearances (
    character_name TEXT,
    appearance TEXT NOT NULL,
    FOREIGN KEY (character_name) REFERENCES character_info(char_name)
);

CREATE TABLE has_background (
    char_name TEXT,
    ch_info TEXT,
    FOREIGN KEY (char_name) REFERENCES media_character(ch_name),
    FOREIGN KEY (ch_info) REFERENCES character_info(char_name)
);

CREATE TABLE crossover (
    game_title TEXT,
    comic_title TEXT,
    character_name TEXT,
    FOREIGN KEY (game_title) REFERENCES game(g_title),
    FOREIGN KEY (comic_title) REFERENCES comic(c_title),
    FOREIGN KEY (Character_name) REFERENCES media_character(ch_name)
);

CREATE TABLE media_has_character (
    character_name TEXT NOT NULL,
    game_title TEXT,
    comic_title TEXT,
    tv_title TEXT,
    movie_title TEXT,
    song_title TEXT,
    FOREIGN KEY (character_name) REFERENCES media_character(ch_name),
    FOREIGN KEY (game_title) REFERENCES game(g_title),
    FOREIGN KEY (comic_title) REFERENCES comic(c_title),
    FOREIGN KEY (tv_title) REFERENCES tv_show(tv_title),
    FOREIGN KEY (movie_title) REFERENCES movie(mo_title),
    FOREIGN KEY (song_title) REFERENCES song(s_title)
);


-- Insertion for initial table values
INSERT INTO posts (title, content)
VALUES 
   ("First Post", "This is my first post"),
   ("Second Post", "This is my second post");

INSERT INTO users (username, passwd, email, phone_no)
VALUES
    ("sam_haj", "ilovecs2300", "sam@mst.edu", 3145551234);

INSERT INTO song (s_title, year_no , favorite, star_amount, media_comment, s_length, s_genre)
VALUES 
   ("Undefeatable", 2022, true, 5, "This song is a banger", 4.24, "Rock"),
   ("Lights, Camera, Action!", 2017, true, 5, "Goes hard", 3.07, "Pop"),
   ("Fist Bump", 2017, false, 3, "It's alright", 4.27, "Rock");

INSERT INTO game (g_title, year_no, favorite, media_comment, star_amount)
VALUES 
   ("Sonic Forces", 2017, true, "Great game", 4.5),
   ("Sonic Mania", 2017, true, "Best Sonic game", 5),
   ("Sonic Heroes", 2003, false, "Not the best Sonic game", 3.5);

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
