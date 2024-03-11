# Задание №6
# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.


# from flask import Flask,request,render_template,redirect,url_for
#
# app = Flask(__name__)
# AGE_LIMIT = 18
#
# @app.route('/',methods=['POST','GET'])
# def index():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         age = int(request.form.get('age'))
#         if age >= AGE_LIMIT:
#             return render_template('result.html',name=name,age=age)
#         else:
#             error = "Нет 18 лет"
#             return render_template('error.html', error=error)
#     return render_template('index.html')
#
# @app.route('/error')
# def error():
#     return render_template('error.html')
#
# app.route('/result')
# def result():
#     name = request.args.get('name')
#     age = request.args.get('age')
#     return render_template('result.html', name=name,age=age)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
AGE_LIMIT = 18

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age >= AGE_LIMIT:
            return redirect(url_for('result', name=name, age=age))
        else:
            error = "Вам нет 18 лет"
            return redirect(url_for('error', error=error))
    return render_template('index.html')

@app.route('/error')
def error():
    error = request.args.get('error')
    return render_template('error.html', error=error)

@app.route('/result')
def result():
    name = request.args.get('name')
    age = request.args.get('age')
    return render_template('result.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)