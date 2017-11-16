from flask import Flask
from models import db

app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'dbtest',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
# print app.config['SQLALCHEMY_DATABASE_URI']
db.init_app(app)

@app.route("/")
def main():
    return 'Hello World ok!'

@app.route("/users", methods = ['GET', 'POST'])
def main():
    return 'Hello World ok!'

if __name__ == '__main__':
    app.run()