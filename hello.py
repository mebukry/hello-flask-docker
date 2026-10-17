from flask import Flask, render_template_string, request

app = Flask(__name__)

PAGE = '''
<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Генератор приветствия</title>
</head>
<body>
    <h1>Генератор приветствия</h1>
    <form method="post">
        <input name="name" placeholder="Введите имя" value="{{ name }}" autofocus>
        <button type="submit">Приветствовать</button>
    </form>
    {% if greeting %}
        <h2>{{ greeting }}</h2>
    {% endif %}
</body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def index():
    greeting = None
    name = ''

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if name:
            greeting = f'Привет, {name}!'
        else:
            greeting = 'Пожалуйста, введи своё имя.'

    return render_template_string(PAGE, greeting=greeting, name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
