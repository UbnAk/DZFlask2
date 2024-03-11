# Задание №4
# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.


from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        post_text = request.form.get('text')
        word_count = len(post_text.split())
        return redirect(f'/result?count={word_count}')
    return render_template('base.html')

@app.route('/result')
def result():
    word_count = request.args.get('count')
    return render_template('result.html', count=word_count)


if __name__ == '__main__':
    app.run(debug=True)

print(a)