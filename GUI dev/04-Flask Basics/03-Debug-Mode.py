from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/information')
def info():
    return '<h1>15-Puzzle Solvability Tester!!</h1>'

@app.route('/user/<name>')
def user(name):
    # Page for an individual user.
    return '<h1>This is a page for {}<h1>'.format(name[50])

if __name__ == '__main__':
    # Never have debug=True for production apps!
    app.run(debug=True) #helps to debug. check the name[50] again.
