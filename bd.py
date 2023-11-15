import sqlite3

db = sqlite3.connect('tetrisofflayt.db')

c = db.cursor()

c.execute("""CREATE TABLE articles (
    title text,
    full_text text,
    wiews integer,
    avtor text
)""")

db.commit()

db.close()