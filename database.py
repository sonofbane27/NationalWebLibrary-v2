from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://uciq7v1hs5kdqvo2ntr0:pscale_pw_eL0jlwrJD0wYmHLX84n33ElLeop869QkrWoyUMCIyrD@aws.connect.psdb.cloud/nationallibrary?charset=utf8mb4"

engine = create_engine(db_connection_string,
                      connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

def load_books_from_db:
with engine.connect() as conn:
  result = conn.execute(text("select * from books"))
  books  = []
  for row in result.all():
    books.append(dict(row))
  return books  
  
