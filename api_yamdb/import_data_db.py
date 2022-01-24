import csv
import sqlite3

path = 'db.sqlite3'

"""con = sqlite3.connect(path)
cur = con.cursor()
with open('D:/Dev/api_yamdb/api_yamdb/static/data/genre.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['name'], i['slug']) for i in dr]
cur.executemany(('INSERT INTO categories_genres (id, name, slug) '
                 'VALUES (?, ?, ?);'), to_db)
con.commit()
con.close()

con = sqlite3.connect(path)
cur = con.cursor()
with open('D:/Dev/api_yamdb/api_yamdb/static/data/category.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['name'], i['slug']) for i in dr]
cur.executemany(('INSERT INTO categories_categories (id, name, slug) '
                 'VALUES (?, ?, ?);'), to_db)
con.commit()
con.close()"""

con = sqlite3.connect(path)
cur = con.cursor()
with open('D:/Dev/api_yamdb/api_yamdb/static/data/titles.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['name'], i['year'], i['category_id']) for i in dr]
cur.executemany(('INSERT INTO categories_title (id, name, year, category_id) '
                 'VALUES (?, ?, ?, ?);'), to_db)
con.commit()
con.close()

con = sqlite3.connect(path)
cur = con.cursor()
with open('D:/Dev/api_yamdb/api_yamdb/static/data/genre_title.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['genre_id'], i['title_id']) for i in dr]
cur.executemany(('INSERT INTO categories_titlesgenres (id, genre_id, title_id) '
                 'VALUES (?, ?, ?);'), to_db)
con.commit()
con.close()

con = sqlite3.connect(path)
cur = con.cursor()
with open('D:/Dev/api_yamdb/api_yamdb/static/data/review.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['text'], i['score'], i['pub_date'],
              i['author_id'], i['title_id']) for i in dr]
cur.executemany(('INSERT INTO reviews_review (id, text, score, pub_date, '
                 'author_id, title_id) VALUES (?, ?, ?, ?, ?, ?);'), to_db)
con.commit()
con.close()

con = sqlite3.connect(path)
cur = con.cursor()
with open('D:/Dev/api_yamdb/api_yamdb/static/data/users.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['username'], i['email'], i['role'], i['bio'],
              i['first_name'], i['last_name']) for i in dr]
cur.executemany(('INSERT INTO users_user (id, username, email, role, bio, '
                 'first_name, last_name) '
                 'VALUES (?, ?, ?, ?, ?, ?, ?);'), to_db)
con.commit()
con.close()

con = sqlite3.connect(path)
cur = con.cursor()
with open('D:/Dev/api_yamdb/api_yamdb/static/data/comments.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['review_id'], i['text'], i['author_id'],
              i['pub_date']) for i in dr]
cur.executemany(('INSERT INTO reviews_comment (id, review_id, text, author_id,'
                 ' pub_date) VALUES (?, ?, ?, ?, ?);'), to_db)
con.commit()
con.close()