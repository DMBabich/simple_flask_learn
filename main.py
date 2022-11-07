from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        action = request.form['operand[]']
        first = float(request.form['input_first'])
        second = float(request.form['input_second'])
        if action == '+':
            answer = first + second
        elif action == '-':
            answer = first - second
        elif action == '*':
            answer = first * second
        elif action == '/':
            answer = first / second
        else:
            answer = 'ERROR'
        result = f'Результат:  {answer}'
        return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True, port=5001)