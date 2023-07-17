from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Create whatever variables you use in python.
    # We can insert it to the html with jinja2 templates!
    return '<h1> Go to /user/name </h1>'

    """_summary_
@app.route('/user/<name>')
def user_name(name):
    # Pass in a user name
    # Pass it to render as a parameter. the html templates may use it as needed with Jinja
    return render_template('01-Template-Variables.html',name=name)
    Returns:
        _type_: _description_
    """


@app.route('/user/<name>')
def user_name(name):
    letters = list(name)
    user_dict = {'user_name':name}
    return render_template('01-Template-Variables.html',
                           name=name,mylist=letters,mydict=user_dict)
    

if __name__ == '__main__':
    app.run(debug=True)
