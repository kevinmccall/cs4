from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/tester')
def tester_page():
    return render_template('tester.html')

    """
    Rewrite the result_page function so that the solvability_result refelcts the solvability of the puzzle.
    
    """
@app.route('/result')
def result_page():
    puzzle = request.args.get('puzzle')
    confidence = request.args.get('user_choice', type=str)
    da_list = json.loads(puzzle)
    even_permutation = is_solvable(da_list)
    result = "solvable" if even_permutation else "not solvable"
    msg = "you are mistaken"
    if confidence == "not sure":
        msg = "Wise answer"
    elif (confidence == "Yes" and even_permutation) or (confidence == "No" and not even_permutation):
        msg = "you are right this time..."
    # match confidence:
    #     case "not sure":
    #         msg = "you are not sure"
    #     case "Yes":
    #         msg = "you are very confident"
    #     case "No":
    #         msg = "u said no."
    return render_template('result.html', puzzle = puzzle, solvability_result=result, nice_message=msg)

""""
# In case you want to create your own 404 page, write a 404 handler.
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
"""    

def is_solvable(input):
    count = 0
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            if input[i] > input[j]:
                count += 1
    return count % 2 == 0

if __name__ == '__main__':
    app.run(debug=True)