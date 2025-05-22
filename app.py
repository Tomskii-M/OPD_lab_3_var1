from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        function='sin',
        angle='',
        unit='degrees',
        precision=2,
        result=None
    )


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        # Получаем данные из формы
        function = request.form.get('function')
        angle = float(request.form.get('angle'))
        unit = request.form.get('unit')
        precision = int(request.form.get('precision'))

        # Конвертируем в радианы если нужно
        if unit == 'degrees':
            angle_rad = math.radians(angle)
        else:
            angle_rad = angle

        # Вычисляем выбранную функцию
        if function == 'sin':
            value = math.sin(angle_rad)
        elif function == 'cos':
            value = math.cos(angle_rad)
        elif function == 'tan':
            value = math.tan(angle_rad)
        elif function == 'cot':
            value = 1 / math.tan(angle_rad)

        # Округляем до заданной точности
        result = round(value, precision)

        return render_template(
            'index.html',
            function=function,
            angle=angle,
            unit=unit,
            precision=precision,
            result=result
        )


if __name__ == '__main__':
    app.run(debug=True)
