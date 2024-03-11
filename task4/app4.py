# Задание №7
# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.


from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        number = int(request.form.get('number'))
        res = number * number
        return redirect(url_for('result', number=number, res=res))
    return render_template('index.html')

@app.route('/result')
def result():
    number = request.args.get('number')
    res = request.args.get('res')
    return render_template('result.html',number=number,res=res)


if __name__ == '__main__':
    app.run(debug=True)
