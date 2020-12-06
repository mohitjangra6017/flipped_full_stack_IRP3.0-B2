from flask import Flask, redirect, url_for,request, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return template('index.html')

if __name__ == '__main__':
    app.run(debug=True)