from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def student():

   return render_template('index.html')


@app.route('/', methods=["POST"])
def register():
       return "User already exists"



if __name__ == '__main__':
   app.run(debug=True)