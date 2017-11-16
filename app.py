from flask import Flask, request
from models import db, Users

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

@app.route("/api/users", methods = ['GET', 'POST'])
def users():
   
    errors = []
    users = {}
    if request.method == "POST":

        if not request.form['user_name']:
            flash('please enter book name')

        else:
           
            try:
                
                users = Users(
                    # user_id = 3,
                    user_name = request.form['user_name'],
                    org_name = request.form['org_name'],
                    org_address = request.form['org_address'],
                    email = request.form['email']
                
                )
                print 'users'
                print users
                db.session.add(users)
                db.session.commit()
            except:
                errors.append("Unable to add in database.")
    return users.user_name            
    # return render_template('index.html', errors=errors, results=results)



if __name__ == '__main__':
    app.run()