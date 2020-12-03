from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Mohit"

@app.route('/login')
def login():
    return "Welcome to login Page"

if __name__ == '__main__':
    app.run()