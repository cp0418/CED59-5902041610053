from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)

@app.route('/')
def student():

   return render_template('index.html')


@app.route('/', methods=["POST"])
def register():
   if request.method == "POST":
      details = request.form
      firstName = details['Name']
      lastName = details['Surname']
      email = details['Email']
      username = details['Username']
      password = details['Password']
      cur = mysql.connection.cursor()

      params = [username]
      count = cur.execute('select * from user where username=%s', params)
      if count == 0:
         cur.execute("INSERT INTO user(firstName, lastName, email, username, password) VALUES (%s, %s, %s, %s,%s)",
                     (firstName, lastName, email, username, password))
         mysql.connection.commit()
         return "Succesfull"
      else:
       return "User already exists"



if __name__ == '__main__':
   app.run(debug=True)