from flask import Flask, render_template

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


@app.route("/")
def hello_world():
  return render_template('home.html')

@app.route("/results")
def search_results():
  return render_template('search.html', books=BOOKS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
