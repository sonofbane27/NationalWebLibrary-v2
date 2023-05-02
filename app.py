from flask import Flask, render_template
from database import engine
from sqlalchemy import text

app = Flask(__name__)

BOOKS = [
{
  'id':'1',
  'title':'In Search of Lost Time',
  'author':'Marcel Proust'
},
{
  'id':'2',
  'title':'Ulysses',
  'author':'James Joyce'
},
{
  'id':'3',
  'title':'The Great Gatsby',
  'author':'F. Scott Fitzgerald'
},
{
  'id':'4',
  'title':'Moby Dick',
  'author':'Herman Melville'
}  
]

def load_books_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from books"))
    books = []
    result_dicts = []
    for row in result.all():
      result_dicts.append(dict(row))
      return books
    

@app.route("/")
def hello_world():
  return render_template('home.html')

@app.route("/api/results")
def search_results():
  books = load_books_from_db()
  return jsonify(books)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
