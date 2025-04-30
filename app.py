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
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_song(s_title):
    conn = get_db_connection()
    songs = conn.execute('SELECT * FROM song WHERE s_title = ?',
                        (s_title,)).fetchone()
    conn.close()
    if songs is None:
        abort(404)
    return songs

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    users = conn.execute('SELECT * FROM users').fetchall()
    song = conn.execute('SELECT * FROM song').fetchall()
    tv_show = conn.execute('SELECT * FROM tv_show').fetchall()
    movie = conn.execute('SELECT * FROM movie').fetchall()
    game = conn.execute('SELECT * FROM game').fetchall()
    comic = conn.execute('SELECT * FROM comic').fetchall()
    conn.close()
    return render_template('index.html', posts=posts, users=users, song=song, movie=movie, game=game, comic=comic, tv_show=tv_show)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')

        elif not content:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit.html', post=post)

# HTML Pages for creating vpages

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

        if not g_title:
            flash('Game title is required!')
        elif not year_no:
            flash('Game year is required!')

        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO game (g_title, year_no, favorite, star_amount, media_comment) VALUES (?, ?, ?, ?, ?)',
                         (g_title, year_no, favorite, star_amount, media_comment))
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

@app.route('/create_start/')
def create_start():
    return render_template('create_start.html')


# HTML Pages for editing values

@app.route('/<int:id>/edit/_song', methods=('GET', 'POST'))
def edit_song(s_title):
    songs = get_song(s_title)

    if request.method == 'POST':
        s_title = request.form['s_title']
        year_no = request.form['year_no']
        favorite = request.form['favorite']
        star_amount = request.form['star_amount']
        media_comment = request.form['media_comment']
        s_length = request.form['s_length']
        s_genre = request.form['s_genre']

        if not s_title:
            flash('Title is required!')

        elif not year_no:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE song SET s_title = ?, year_no = ?, favorite = ?, star_amount = ?, media_comment = ?, s_length = ?, s_genre = ?'
                         ' WHERE s_title = ?',
                         (s_title, year_no, favorite, star_amount, media_comment, s_length, s_genre))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit_song.html', songs=songs)