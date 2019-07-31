from flask import Flask
app = Flask(__name__) #__name__ = filename
@app.route('/')
def index():

    return "hello World"

if __name__=='__main__':
    app.run() #app is object from flask