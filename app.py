#Imports and initializations
from flask import Flask, render_template, request, url_for, flash, redirect, abort
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SonicFansUnite'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

#Fetching data from the entities
def get_song(id):
    conn = get_db_connection()
    songs = conn.execute('SELECT * FROM song WHERE id = ?',
                        (id,)).fetchone()
    conn.close()
    if songs is None:
        abort(404)
    return songs

def get_comic(id):
    conn = get_db_connection()
    comics = conn.execute('SELECT * FROM comic WHERE id = ?',
                        (id,)).fetchone()
    conn.close()
    if comics is None:
        abort(404)
    return comics

def get_tvshow(id):
    conn = get_db_connection()
    tvs = conn.execute('SELECT * FROM tv_show WHERE id = ?',
                        (id,)).fetchone()
    conn.close()
    if tvs is None:
        abort(404)
    return tvs

def get_movie(id):
    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movie WHERE id = ?',
                        (id,)).fetchone()
    conn.close()
    if movies is None:
        abort(404)
    return movies

def get_game(id):
    conn = get_db_connection()
    games = conn.execute('SELECT * FROM game WHERE id = ?',
                        (id,)).fetchone()
    conn.close()
    if games is None:
        abort(404)
    return games

def get_char(id):
    conn = get_db_connection()
    chars = conn.execute('SELECT * FROM media_character WHERE id = ?',
                        (id,)).fetchone()
    conn.close()
    if chars is None:
        abort(404)
    return chars


#"Home" pages
@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    song = conn.execute('SELECT * FROM song').fetchall()
    tv_show = conn.execute('SELECT * FROM tv_show').fetchall()
    movie = conn.execute('SELECT * FROM movie').fetchall()
    game = conn.execute('SELECT * FROM game').fetchall()
    comic = conn.execute('SELECT * FROM comic').fetchall()
    media_character = conn.execute('SELECT * FROM media_character').fetchall()
    conn.close()
    return render_template('index.html', users=users, song=song, movie=movie, game=game, comic=comic, tv_show=tv_show, media_character=media_character)

@app.route('/relationships/')
def relationships():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    song = conn.execute('SELECT * FROM song').fetchall()
    tv_show = conn.execute('SELECT * FROM tv_show').fetchall()
    movie = conn.execute('SELECT * FROM movie').fetchall()
    game = conn.execute('SELECT * FROM game').fetchall()
    comic = conn.execute('SELECT * FROM comic').fetchall()
    media_character = conn.execute('SELECT * FROM media_character').fetchall()
    conn.close()
    return render_template('relationships.html', users=users, song=song, movie=movie, game=game, comic=comic, tv_show=tv_show, media_character=media_character)


#Pages for creating new entities
@app.route('/create_song/', methods=('GET', 'POST'))
def create_song():
    if request.method == 'POST':
        s_title = request.form['s_title']
        year_no = request.form['year_no']
        favorite = request.form['favorite']
        star_amount = request.form['star_amount']
        media_comment = request.form['media_comment']
        s_length = request.form['s_length']
        s_genre = request.form['s_genre']
        s_singer = request.form['s_singer']

        if not s_title:
            flash('Song title is required!')
        elif not year_no:
            flash('Song year is required!')
        elif not s_length:
            flash('Song length is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO song (s_title, year_no, favorite, star_amount, media_comment, s_length, s_genre) VALUES (?, ?, ?, ?, ?, ?, ?)',
                         (s_title, year_no, favorite, star_amount, media_comment, s_length, s_genre))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create_song.html')

@app.route('/create_movie/', methods=('GET', 'POST'))
def create_movie():
    if request.method == 'POST':
        mo_title = request.form['mo_title']
        year_no = request.form['year_no']
        favorite = request.form['favorite']
        star_amount = request.form['star_amount']
        media_comment = request.form['media_comment']
        mo_director = request.form['mo_director']

        if not mo_title:
            flash('Movie title is required!')
        elif not year_no:
            flash('Movie year is required!')
        elif not mo_director:
            flash('Movie director is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO movie (mo_title, year_no, favorite, star_amount, media_comment, mo_director) VALUES (?, ?, ?, ?, ?, ?)',
                         (mo_title, year_no, favorite, star_amount, media_comment, mo_director))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create_movie.html')

@app.route('/create_game/', methods=('GET', 'POST'))
def create_game():
    if request.method == 'POST':
        g_title = request.form['g_title']
        year_no = request.form['year_no']
        favorite = request.form['favorite']
        star_amount = request.form['star_amount']
        media_comment = request.form['media_comment']
        g_genre = request.form['g_genre']

        if not g_title:
            flash('Game title is required!')
        elif not year_no:
            flash('Game year is required!')

        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO game (g_title, year_no, favorite, star_amount, media_comment, g_genre) VALUES (?, ?, ?, ?, ?, ?)',
                         (g_title, year_no, favorite, star_amount, media_comment, g_genre))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create_game.html')

@app.route('/create_comic/', methods=('GET', 'POST'))
def create_comic():
    if request.method == 'POST':
        c_title = request.form['c_title']
        year_no = request.form['year_no']
        favorite = request.form['favorite']
        star_amount = request.form['star_amount']
        media_comment = request.form['media_comment']
        c_series = request.form['c_series']

        if not c_title:
            flash('Comic title is required!')
        elif not year_no:
            flash('Comic year is required!')
        elif not c_series:
            flash('Comic series is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO comic (c_title, year_no, favorite, star_amount, media_comment, c_series) VALUES (?, ?, ?, ?, ?, ?)',
                         (c_title, year_no, favorite, star_amount, media_comment, c_series))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create_comic.html')

@app.route('/create_tvshow/', methods=('GET', 'POST'))
def create_tvshow():
    if request.method == 'POST':
        tv_title = request.form['tv_title']
        year_no = request.form['year_no']
        favorite = request.form['favorite']
        star_amount = request.form['star_amount']
        media_comment = request.form['media_comment']
        tv_season_count = request.form['tv_season_count']
        is_cgi = request.form['is_cgi']
        is_animated = request.form['is_animated']

        if not tv_title:
            flash('TV show title is required!')
        elif not year_no:
            flash('TV show release year is required!')
        elif not tv_season_count:
            flash('Tv show season count is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO tv_show (tv_title, year_no, favorite, star_amount, media_comment, tv_season_count, is_cgi, is_animated) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                         (tv_title, year_no, favorite, star_amount, media_comment, tv_season_count, is_cgi, is_animated))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create_tvshow.html')

@app.route('/create_character/', methods=('GET', 'POST'))
def create_character():
    if request.method == 'POST':
        ch_name = request.form['ch_name']
        species = request.form['species']
        fur_color = request.form['fur_color']
        eye_color = request.form['eye_color']
        fluff_color = request.form['fluff_color']

        if not ch_name:
            flash('Character name is required!')
        elif not species:
            flash('Species is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO media_character (ch_name, species, fur_color, eye_color, fluff_color) VALUES (?, ?, ?, ?, ?)',
                         (ch_name, species, fur_color, eye_color, fluff_color))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create_character.html')



#Pages for creating new relationships
@app.route('/create_crossover/', methods=('GET', 'POST'))
def create_crossover():
    conn = get_db_connection()
    game = conn.execute('SELECT * FROM game').fetchall()
    comic = conn.execute('SELECT * FROM comic').fetchall()
    media_character = conn.execute('SELECT * FROM media_character').fetchall()
    if request.method == 'POST':
        g_id = request.form['g_id']
        c_id = request.form['c_id']
        char_id = request.form['char_id']

        if not g_id:
            flash('Game ID is required!')
        elif not year_no:
            flash('Comic ID is required!')
        elif not tv_season_count:
            flash('Character ID is required!')
        else:
            conn.execute('INSERT INTO crossover (g_id, c_id, char_id) VALUES (?, ?, ?)',
                         (g_id, c_id, char_id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create_crossover.html', game=game, comic=comic, media_character=media_character)

@app.route('/create_media_w_char/', methods=('GET', 'POST'))
def create_media_w_char():
    if request.method == 'POST':
        ch_id = request.form['ch_id']
        g_id = request.form['g_id']
        c_id = request.form['c_id']
        tv_id = request.form['tv_id']
        mo_id = request.form['mo_id']
        s_id = request.form['s_id']

        if not ch_id:
            flash('Character ID is required!')
        
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO media_has_character (ch_id, g_id, c_id, tv_id, mo_id, s_id) VALUES (?, ?, ?, ?, ?, ?)',
                         (ch_id, g_id, c_id, tv_id, mo_id, s_id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create_media_w_char.html')

@app.route('/create_has_bg/', methods=('GET', 'POST'))
def create_has_bg():
    if request.method == 'POST':
        char_id = request.form['char_id']
        ch_info_id = request.form['ch_info_id']

        if not ch_id:
            flash('Character ID is required!')
        elif not ch_info_id:
            flash('Character info ID is required!')
        
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO has_background (char_id, ch_info_id) VALUES (?, ?)',
                         (char_id, ch_info_id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create_has_bg.html')

@app.route('/create_interacted/', methods=('GET', 'POST'))
def create_interacted():
    if request.method == 'POST':
        u_username = request.form['u_username']
        mo_id = request.form['mo_id']
        c_id = request.form['c_id']
        s_id = request.form['s_id']
        g_id = request.form['g_id']
        tv_id = request.form['tv_id']
        date_of_interaction = request.form['date_of_interaction']

        if not u_username:
            flash('Username is required!')
        elif not date_of_interaction:
            flash('First date interacted is required!')
        
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO interacted_with (u_username, mo_id, c_id, s_id, g_id, tv_id, date_of_interaction) VALUES (?, ?, ?, ?, ?, ?, ?)',
                         (u_username, mo_id, c_id, s_id, g_id, tv_id, date_of_interaction))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create_interacted.html')

@app.route('/create_comic_artist/', methods=('GET', 'POST'))
def create_comic_artist():
    conn = get_db_connection()
    comic = conn.execute('SELECT * FROM comic').fetchall()
    if request.method == 'POST':
        c_id = request.form['c_id']
        c_artist = request.form['c_artist']

        if not c_id:
            flash('Comic ID is required!')
        elif not c_artist:
            flash('Comic artist is required!')
        
        else:
            conn.execute('INSERT INTO comic_artists (c_id, c_artist) VALUES (?, ?)',
                         (c_id, c_artist))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create_comic_artist.html', comic=comic)



#Pages for editing values
@app.route('/<int:id>/edit_song/', methods=('GET', 'POST'))
def edit_song(id):
    songs = get_song(id)

    if request.method == 'POST':
        s_title = request.form['s_title']
        year_no = request.form['year_no']
        favorite = request.form['favorite']
        star_amount = request.form['star_amount']
        media_comment = request.form['media_comment']
        s_length = request.form['s_length']
        s_genre = request.form['s_genre']
        s_singer = request.form['s_singer']

        if not s_title:
            flash('Title is required!')

        elif not year_no:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE song SET s_title = ?, year_no = ?, favorite = ?, star_amount = ?, media_comment = ?, s_length = ?, s_genre = ?, s_singer = ?'
                         ' WHERE id = ?',
                         (s_title, year_no, favorite, star_amount, media_comment, s_length, s_genre, s_singer, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit_song.html', songs=songs)

@app.route('/<int:id>/edit_comic/', methods=('GET', 'POST'))
def edit_comic(id):
    comics = get_comic(id)

    if request.method == 'POST':
        c_title = request.form['c_title']
        year_no = request.form['year_no']
        favorite = request.form['favorite']
        star_amount = request.form['star_amount']
        media_comment = request.form['media_comment']
        c_series = request.form['c_series']

        if not c_title:
            flash('Title is required!')

        elif not year_no:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE comic SET c_title = ?, year_no = ?, favorite = ?, star_amount = ?, media_comment = ?, c_series = ?'
                         ' WHERE id = ?',
                         (c_title, year_no, favorite, star_amount, media_comment, c_series, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit_comic.html', comics=comics)

@app.route('/<int:id>/edit_tvshow/', methods=('GET', 'POST'))
def edit_tvshow(id):
    tvs = get_tvshow(id)

    if request.method == 'POST':
        tv_title = request.form['tv_title']
        year_no = request.form['year_no']
        favorite = request.form['favorite']
        star_amount = request.form['star_amount']
        media_comment = request.form['media_comment']
        is_cgi = request.form['is_cgi']
        is_animated = request.form['is_animated']

        if not tv_title:
            flash('Title is required!')

        elif not year_no:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE tv_show SET tv_title = ?, year_no = ?, favorite = ?, star_amount = ?, media_comment = ?, is_cgi = ?, is_animated = ?'
                         ' WHERE id = ?',
                         (tv_title, year_no, favorite, star_amount, media_comment, is_cgi, is_animated, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit_tvshow.html', tvs=tvs)

@app.route('/<int:id>/edit_movie/', methods=('GET', 'POST'))
def edit_movie(id):
    movies = get_movie(id)

    if request.method == 'POST':
        mo_title = request.form['mo_title']
        year_no = request.form['year_no']
        favorite = request.form['favorite']
        star_amount = request.form['star_amount']
        media_comment = request.form['media_comment']
        mo_director = request.form['mo_director']

        if not mo_title:
            flash('Title is required!')

        elif not year_no:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE movie SET mo_title = ?, year_no = ?, favorite = ?, star_amount = ?, media_comment = ?, mo_director = ?'
                         ' WHERE id = ?',
                         (mo_title, year_no, favorite, star_amount, media_comment, mo_director, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit_movie.html', movies=movies)

@app.route('/<int:id>/edit_game/', methods=('GET', 'POST'))
def edit_game(id):
    games = get_game(id)

    if request.method == 'POST':
        g_title = request.form['g_title']
        year_no = request.form['year_no']
        favorite = request.form['favorite']
        star_amount = request.form['star_amount']
        media_comment = request.form['media_comment']
        g_genre = request.form['g_genre']

        if not g_title:
            flash('Title is required!')

        elif not year_no:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE game SET g_title = ?, year_no = ?, favorite = ?, star_amount = ?, media_comment = ?'
                         ' WHERE id = ?',
                         (g_title, year_no, favorite, star_amount, media_comment, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit_game.html', games=games)

@app.route('/<int:id>/edit_character/', methods=('GET', 'POST'))
def edit_character(id):
    chars = get_char(id)

    if request.method == 'POST':
        ch_name = request.form['ch_name']
        species = request.form['species']
        fur_color = request.form['fur_color']
        eye_color = request.form['eye_color']
        fluff_color = request.form['fluff_color']

        if not ch_name:
            flash('Name is required!')
        elif not species:
            flash('Species is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE media_character SET ch_name = ?, species = ?, fur_color = ?, eye_color = ?, fluff_color = ?'
                         ' WHERE id = ?',
                         (ch_name, species, fur_color, eye_color, fluff_color, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit_character.html', chars=chars)


#Pages for deleting values
@app.route('/<int:id>/delete_game/', methods=('POST',))
def delete_game(id):
    games = get_game(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM game WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/<int:id>/delete_movie/', methods=('POST',))
def delete_movie(id):
    movies = get_movie(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM movie WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/<int:id>/delete_song/', methods=('POST',))
def delete_song(id):
    songs = get_song(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM song WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/<int:id>/delete_tvshow/', methods=('POST',))
def delete_tvshow(id):
    tvs = get_tvshow(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM tv_show WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/<int:id>/delete_comic/', methods=('POST',))
def delete_comic(id):
    comics = get_comic(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM comic WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/<int:id>/delete_char/', methods=('POST',))
def delete_char(id):
    chars = get_char(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM media_character WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
