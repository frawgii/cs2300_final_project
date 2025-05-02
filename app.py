#Imports and initializations
from flask import Flask, render_template, request, url_for, flash, redirect, abort
import sqlite3

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

def get_crossover(id):
    conn = get_db_connection()
    crosses = conn.execute('SELECT * FROM crossover WHERE g_id = ? AND c_id = ? AND char_id = ?',
                        (id,)).fetchone()
    conn.close()
    if crosses is None:
        abort(404)
    return crosses


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
            song_id = conn.execute('SELECT s.id FROM song s WHERE s.s_title=s_title').fetchone()
            one_id = song_id[0]
            conn.execute('INSERT INTO interacted_with (u_username, s_id) VALUES (?, ?)',
                         ('sam_haj', int(one_id)))
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
            mo_id = conn.execute('SELECT mo.id FROM movie mo WHERE mo.mo_title=mo_title').fetchone()
            one_id = mo_id[0]
            conn.execute('INSERT INTO interacted_with (u_username, mo_id) VALUES (?, ?)',
                         ('sam_haj', int(one_id)))
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
            game_id = conn.execute('SELECT g.id FROM game g WHERE g.g_title=g_title').fetchone()
            one_id = game_id[0]
            conn.execute('INSERT INTO interacted_with (u_username, g_id) VALUES (?, ?)',
                         ('sam_haj', int(one_id)))
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
            comic_id = conn.execute('SELECT c.id FROM comic c WHERE c.c_title=c_title').fetchone()
            one_id = comic_id[0]
            conn.execute('INSERT INTO interacted_with (u_username, c_id) VALUES (?, ?)',
                         ('sam_haj', int(one_id)))
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
            tv_id = conn.execute('SELECT tv.id FROM tv_show tv WHERE tv.tv_title=tv_title').fetchone()
            one_id = tv_id[0]
            conn.execute('INSERT INTO interacted_with (u_username, tv_id) VALUES (?, ?)',
                         ('sam_haj', int(one_id)))
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
        elif not c_id:
            flash('Comic ID is required!')
        elif not char_id:
            flash('Character ID is required!')
        else:
            conn.execute('INSERT INTO crossover (g_id, c_id, char_id) VALUES (?, ?, ?)',
                         (g_id, c_id, char_id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create_crossover.html', game=game, comic=comic, media_character=media_character)

@app.route('/create_animator/', methods=('GET', 'POST'))
def create_animator():
    conn = get_db_connection()
    movie = conn.execute('SELECT * FROM movie').fetchall()
    if request.method == 'POST':
        tv_id = request.form['tv_id']
        anim_animator = request.form['anim_animator']

        if not tv_id:
            flash('TV ID is required!')
        elif not anim_animator:
            flash('Animator name is required!')

        else:
            conn.execute('INSERT INTO anim_animators (tv_id, anim_animator) VALUES (?, ?)',
                         (tv_id, anim_animator))
            conn.commit()
            conn.close()
            return redirect(url_for('relationships'))
    return render_template('create_animator.html', movie=movie)

@app.route('/create_cgi_actor/', methods=('GET', 'POST'))
def create_cgi_actor():
    conn = get_db_connection()
    tv_show = conn.execute('SELECT * FROM tv_show').fetchall()
    if request.method == 'POST':
        tv_id = request.form['tv_id']
        cgi_actor = request.form['cgi_actor']

        if not tv_id:
            flash('TV ID is required!')
        elif not cgi_actor:
            flash('Actor name is required!')

        else:
            conn.execute('INSERT INTO cgi_actors (tv_id, cgi_actor) VALUES (?, ?)',
                         (tv_id, cgi_actor))
            conn.commit()
            conn.close()
            return redirect(url_for('relationships'))
    return render_template('create_cgi_actor.html', tv_show=tv_show)

@app.route('/create_movie_actor/', methods=('GET', 'POST'))
def create_movie_actor():
    conn = get_db_connection()
    movie = conn.execute('SELECT * FROM movie').fetchall()
    if request.method == 'POST':
        mo_id = request.form['mo_id']
        mo_actor = request.form['mo_actor']

        if not mo_id:
            flash('Movie ID is required!')
        elif not mo_actor:
            flash('Actor name is required!')

        else:
            conn.execute('INSERT INTO movie_actors (mo_id, mo_actor) VALUES (?, ?)',
                         (mo_id, mo_actor))
            conn.commit()
            conn.close()
            return redirect(url_for('relationships'))
    return render_template('create_movie_actor.html', movie=movie)

@app.route('/create_m_has_c/', methods=('GET', 'POST'))
def create_m_has_c():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    song = conn.execute('SELECT * FROM song').fetchall()
    tv_show = conn.execute('SELECT * FROM tv_show').fetchall()
    movie = conn.execute('SELECT * FROM movie').fetchall()
    game = conn.execute('SELECT * FROM game').fetchall()
    comic = conn.execute('SELECT * FROM comic').fetchall()
    media_character = conn.execute('SELECT * FROM media_character').fetchall()
    if request.method == 'POST':
        ch_id = request.form['ch_id']
        mo_id = request.form['mo_id']
        c_id = request.form['c_id']
        s_id = request.form['s_id']
        g_id = request.form['g_id']
        tv_id = request.form['tv_id']

        if not ch_id:
            flash('Character ID is required!')
        
        else:
            
            conn.execute('INSERT INTO media_has_character (ch_id, g_id, c_id, tv_id, mo_id, s_id) VALUES (?, ?, ?, ?, ?, ?)',
                         (ch_id, g_id, c_id, tv_id, mo_id, s_id))
            conn.commit()
            conn.close()
            return redirect(url_for('relationships'))
    return render_template('create_m_has_c.html', users=users, song=song, movie=movie, game=game, comic=comic, tv_show=tv_show, media_character=media_character)

@app.route('/create_character_info/', methods=('GET', 'POST'))
def create_character_info():
    conn = get_db_connection()
    media_character = conn.execute('SELECT * FROM media_character').fetchall()
    if request.method == 'POST':
        char_id = request.form['char_id']
        journal_entry = request.form['journal_entry']
        abilities = request.form['abilities']
        appearance = request.form['appearance']

        if not ch_id:
            flash('Character ID is required!')
        elif not journal_entry:
            flash('Journal entry is required!')
        
        else:
            
            conn.execute('INSERT INTO character_info (char_id, journal_entry, abilities, appearance) VALUES (?, ?, ?, ?)',
                         (char_id, journal_entry, abilities, appearance))
            conn.commit()
            conn.close()
            return redirect(url_for('relationships'))
    return render_template('create_character_info.html', media_character=media_character)

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


# SQL QUERIES TO EXECUTE
@app.route('/queries/', methods=('GET', 'POST'))
def queries():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    song = conn.execute('SELECT * FROM song').fetchall()
    tv_show = conn.execute('SELECT * FROM tv_show').fetchall()
    movie = conn.execute('SELECT * FROM movie').fetchall()
    game = conn.execute('SELECT * FROM game').fetchall()
    comic = conn.execute('SELECT * FROM comic').fetchall()
    media_character = conn.execute('SELECT * FROM media_character').fetchall()
    interacted_with = conn.execute('SELECT * FROM interacted_with').fetchall()
    curs = conn.cursor()
    curs.execute('SELECT sum(s.s_length) FROM song s')
    sum_len = curs.fetchone()[0]
    curs.execute('SELECT avg(s.s_length) FROM song s')
    avg_len = curs.fetchone()[0]
    curs.execute('SELECT avg(s.star_amount + m.star_amount + g.star_amount + c.star_amount + tv.star_amount)/5.0 FROM song s, movie m, game g, comic c, tv_show tv')
    avg_star = curs.fetchone()[0]
    curs.execute('SELECT min(min(s.star_amount), min(m.star_amount), min(g.star_amount), min(c.star_amount), min(tv.star_amount)) FROM song s, movie m, game g, comic c, tv_show tv')
    min_star = curs.fetchone()[0]
    curs.execute('SELECT max(max(s.star_amount), max(m.star_amount), max(g.star_amount), max(c.star_amount), max(tv.star_amount)) FROM song s, movie m, game g, comic c, tv_show tv')
    max_star = curs.fetchone()[0]
    curs.execute('SELECT min(min(s.year_no), min(m.year_no), min(g.year_no), min(c.year_no), min(tv.year_no)) FROM song s, movie m, game g, comic c, tv_show tv')
    min_year = curs.fetchone()[0]
    curs.execute('SELECT max(max(s.year_no), max(m.year_no), max(g.year_no), max(c.year_no), max(tv.year_no)) FROM song s, movie m, game g, comic c, tv_show tv')
    max_year = curs.fetchone()[0]
    curs.execute('SELECT count(*) FROM interacted_with')
    row_count = curs.fetchone()[0]
    curs.execute('SELECT g_title FROM game g WHERE g.favorite = 1')
    fav_g = curs.fetchall()
    curs.execute('SELECT c_title FROM comic c WHERE c.favorite = 1')
    fav_c = curs.fetchall()
    curs.execute('SELECT tv_title FROM tv_show tv WHERE tv.favorite = 1')
    fav_tv = curs.fetchall()
    curs.execute('SELECT mo_title FROM movie mo WHERE mo.favorite = 1')
    fav_mo = curs.fetchall()
    curs.execute('SELECT s_title FROM song s WHERE s.favorite = 1')
    fav_s = curs.fetchall()
    curs.execute('SELECT DISTINCT cgi.cgi_actor FROM cgi_actors cgi, tv_show tv, movie mo, movie_actors ma WHERE cgi.tv_id = tv.id AND mo.id = ma.mo_id AND cgi.cgi_actor = ma.mo_actor')
    actor_list = curs.fetchall()
    #curs.execute('SELECT ch.ch_name FROM media_character ch WHERE NOT EXISTS ((SELECT m.ch_id FROM media_has_character m) EXCEPT (SELECT mc.id FROM media_character mc WHERE ch.id=mc.id))')
    #all_char = curs.fetchall()
    conn.commit()
    conn.close()
    return render_template('queries.html', sum_len=sum_len, avg_len=avg_len, avg_star=avg_star, min_star=min_star, max_star=max_star,\
                             min_year=min_year, max_year=max_year, row_count=row_count, fav_g=fav_g, fav_c=fav_c, fav_tv=fav_tv,\
                              fav_mo=fav_mo, fav_s=fav_s, actor_list=actor_list)

@app.route('/song_queries/', methods=('GET', 'POST'))
def song_queries():
    conn = get_db_connection()
    curs = conn.cursor()
    curs.execute('SELECT sum(s.s_length) FROM song s')
    sum_len = curs.fetchone()[0]
    curs.execute('SELECT avg(s.s_length) FROM song s')
    avg_len = curs.fetchone()[0]
    curs.execute('SELECT avg(s.star_amount) FROM song s')
    avg_star = curs.fetchone()[0]
    curs.execute('SELECT min(s.star_amount) FROM song s')
    min_star = curs.fetchone()[0]
    curs.execute('SELECT max(s.star_amount) FROM song s')
    max_star = curs.fetchone()[0]
    curs.execute('SELECT min(s.year_no)FROM song s')
    min_year = curs.fetchone()[0]
    curs.execute('SELECT max(s.year_no)FROM song s')
    max_year = curs.fetchone()[0]
    curs.execute('SELECT count(*) FROM song s')
    row_count = curs.fetchone()[0]
    conn.commit()
    conn.close()
    return render_template('song_queries.html', sum_len=sum_len, avg_len=avg_len, avg_star=avg_star, min_star=min_star, max_star=max_star,\
                             min_year=min_year, max_year=max_year, row_count=row_count)

@app.route('/movie_queries/', methods=('GET', 'POST'))
def movie_queries():
    conn = get_db_connection()
    curs = conn.cursor()
    curs.execute('SELECT avg(mo.star_amount) FROM movie mo')
    avg_star = curs.fetchone()[0]
    curs.execute('SELECT min(mo.star_amount) FROM movie mo')
    min_star = curs.fetchone()[0]
    curs.execute('SELECT max(mo.star_amount) FROM movie mo')
    max_star = curs.fetchone()[0]
    curs.execute('SELECT min(mo.year_no)FROM movie mo')
    min_year = curs.fetchone()[0]
    curs.execute('SELECT max(mo.year_no)FROM movie mo')
    max_year = curs.fetchone()[0]
    curs.execute('SELECT count(*) FROM movie mo')
    row_count = curs.fetchone()[0]
    conn.commit()
    conn.close()
    return render_template('movie_queries.html', avg_star=avg_star, min_star=min_star, max_star=max_star,\
                             min_year=min_year, max_year=max_year, row_count=row_count)

@app.route('/tv_queries/', methods=('GET', 'POST'))
def tv_queries():
    conn = get_db_connection()
    curs = conn.cursor()
    curs.execute('SELECT avg(tv.star_amount) FROM tv_show tv')
    avg_star = curs.fetchone()[0]
    curs.execute('SELECT min(tv.star_amount) FROM tv_show tv')
    min_star = curs.fetchone()[0]
    curs.execute('SELECT max(tv.star_amount) FROM tv_show tv')
    max_star = curs.fetchone()[0]
    curs.execute('SELECT min(tv.year_no)FROM tv_show tv')
    min_year = curs.fetchone()[0]
    curs.execute('SELECT max(tv.year_no)FROM tv_show tv')
    max_year = curs.fetchone()[0]
    curs.execute('SELECT count(*) FROM tv_show tv')
    row_count = curs.fetchone()[0]
    conn.commit()
    conn.close()
    return render_template('tv_queries.html', avg_star=avg_star, min_star=min_star, max_star=max_star,\
                             min_year=min_year, max_year=max_year, row_count=row_count)

@app.route('/comic_queries/', methods=('GET', 'POST'))
def comic_queries():
    conn = get_db_connection()
    curs = conn.cursor()
    curs.execute('SELECT avg(c.star_amount) FROM comic c')
    avg_star = curs.fetchone()[0]
    curs.execute('SELECT min(c.star_amount) FROM comic c')
    min_star = curs.fetchone()[0]
    curs.execute('SELECT max(c.star_amount) FROM comic c')
    max_star = curs.fetchone()[0]
    curs.execute('SELECT min(c.year_no)FROM comic c')
    min_year = curs.fetchone()[0]
    curs.execute('SELECT max(c.year_no)FROM comic c')
    max_year = curs.fetchone()[0]
    curs.execute('SELECT count(*) FROM comic c')
    row_count = curs.fetchone()[0]
    conn.commit()
    conn.close()
    return render_template('comic_queries.html', avg_star=avg_star, min_star=min_star, max_star=max_star,\
                             min_year=min_year, max_year=max_year, row_count=row_count)

@app.route('/game_queries/', methods=('GET', 'POST'))
def game_queries():
    conn = get_db_connection()
    curs = conn.cursor()
    curs.execute('SELECT avg(g.star_amount) FROM game g')
    avg_star = curs.fetchone()[0]
    curs.execute('SELECT min(g.star_amount) FROM game g')
    min_star = curs.fetchone()[0]
    curs.execute('SELECT max(g.star_amount) FROM game g')
    max_star = curs.fetchone()[0]
    curs.execute('SELECT min(g.year_no)FROM game g')
    min_year = curs.fetchone()[0]
    curs.execute('SELECT max(g.year_no)FROM game g')
    max_year = curs.fetchone()[0]
    curs.execute('SELECT count(*) FROM game g')
    row_count = curs.fetchone()[0]
    conn.commit()
    conn.close()
    return render_template('game_queries.html', avg_star=avg_star, min_star=min_star, max_star=max_star,\
                             min_year=min_year, max_year=max_year, row_count=row_count)

#Pages with big/interesting queries
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
    curs = conn.cursor()
    curs.execute('SELECT g.g_title AS gt, c.c_title AS ct, ch.ch_name AS cht\
                 FROM crossover co, game g, comic c, media_character ch \
                 WHERE co.g_id = g.id AND co.c_id = c.id AND co.char_id = ch.id')
    crosses = curs.fetchall()
    conn.close()
    return render_template('relationships.html', users=users, song=song, movie=movie,\
                            game=game, comic=comic, tv_show=tv_show, media_character=media_character, \
                            crosses=crosses)

@app.route('/more_info/')
def more_info():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    song = conn.execute('SELECT * FROM song s').fetchall()
    cgi_shows = conn.execute('SELECT * FROM tv_show tv, cgi_actors cgi WHERE tv.is_cgi=1 AND tv.id=cgi.tv_id').fetchall()
    anim_shows = conn.execute('SELECT * FROM tv_show tv, anim_animators a WHERE tv.is_animated=1 AND tv.id=a.tv_id').fetchall()
    movie = conn.execute('SELECT * FROM movie m, movie_actors ma WHERE ma.mo_id=m.id').fetchall()
    game = conn.execute('SELECT * FROM game').fetchall()
    comic = conn.execute('SELECT * FROM comic c, comic_artists ca WHERE c.id=ca.c_id').fetchall()
    media_character = conn.execute('SELECT * FROM media_character m, character_info c WHERE c.char_id=m.id').fetchall()
    conn.close()
    return render_template('more_info.html', users=users, song=song, cgi_shows=cgi_shows, movie=movie,\
                            game=game, anim_shows=anim_shows, comic=comic, media_character=media_character)


#User driven queries
@app.route('/find_m_w_c/', methods=('GET', 'POST'))
def find_m_w_c():
    if request.method == 'POST':
        mch_name = request.form['ch_name']
        conn = get_db_connection()
        curs = conn.cursor()
        curs.execute('SELECT m.c_id, m.mo_id, m.g_id, m.tv_id, m.s_id FROM media_has_character m, media_character c \
                     WHERE m.ch_id=c.id AND c.ch_name=?', (mch_name,))
        media = curs.fetchall()
        for i in media:
            if i['g_id'] != None:
                flash('Game ID: ' + str(i['g_id']))
            elif i['c_id'] != None:
                flash('Comic ID: ' + str(i['c_id']))
            elif i['tv_id'] != None:
                flash('TV ID: ' + str(i['tv_id']))
            elif i['s_id'] != None:
                flash('Song ID: ' + str(i['s_id']))
            elif i['mo_id'] != None:
                flash('Movie ID: ' + str(i['mo_id']))
        conn.commit()
        conn.close()
        return redirect(url_for('find_m_w_c'))
    return render_template('find_m_w_c.html')

@app.route('/find_c_w_f/', methods=('GET', 'POST'))
def find_c_w_f():
    if request.method == 'POST':
        cfur_color = request.form['fur_color']
        conn = get_db_connection()
        curs = conn.cursor()
        curs.execute('SELECT c.ch_name FROM media_character c WHERE fur_color=?', (cfur_color,))
        chars = curs.fetchall()
        for i in chars:
            flash('Character Name: ' + str(i['ch_name']))
        conn.commit()
        conn.close()
        return redirect(url_for('find_c_w_f'))
    return render_template('find_c_w_f.html')

@app.route('/find_c_w_s/', methods=('GET', 'POST'))
def find_c_w_s():
    if request.method == 'POST':
        cspecies = request.form['species']
        conn = get_db_connection()
        curs = conn.cursor()
        curs.execute('SELECT c.ch_name FROM media_character c WHERE species=?', (cspecies,))
        chars = curs.fetchall()
        for i in chars:
            flash('Character Name: ' + str(i['ch_name']))
        conn.commit()
        conn.close()
        return redirect(url_for('find_c_w_s'))
    return render_template('find_c_w_s.html')




