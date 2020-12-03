from flask import Flask
app = Flask(__name__)

@app.route('/hello_singh')
def index():
    return "Hello Mohit"

if __name__ == '__main__':
    app.run()