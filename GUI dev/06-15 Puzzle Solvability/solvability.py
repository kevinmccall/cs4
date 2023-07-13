from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    puzzle = request.args.get('puzzle')
    guess = request.args.get('user_choice')
    
    if guess!= 'not sure':
        return render_template('tester.html', puzzle = puzzle, guess = guess)
    else:
        return render_template('base.html')
    

if __name__ == '__main__':
    app.run(debug=True)