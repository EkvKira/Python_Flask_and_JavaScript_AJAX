from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculator', methods=['POST'])
def calculator():
    try:
        number1_str = request.form['number1']
        number2_str = request.form['number2']
        operation = request.form['operation']

        if not number1_str or not number1_str.replace('.', '').isdigit():
            error_message = "Entrada no válida para el primer número. Por favor, proporcione un valor numérico válido."
            return error_message

        if not number2_str or not number2_str.replace('.', '').isdigit():
            error_message = "Entrada no válida para el segundo número. Por favor, proporcione un valor numérico válido."
            return error_message

        number1 = float(number1_str)
        number2 = float(number2_str)
    except KeyError:
        error_message = "Falta 'primer número', 'segundo número' u 'operación' en la solicitud."
        return error_message
    except ValueError:
        error_message = "Entrada no válida. Por favor, proporcione valores numéricos válidos para 'primer número' y 'segundo número'."
        return error_message

    if operation == 'multiply':
        result = number1 * number2
    elif operation == 'divide':
        result = number1 / number2
    elif operation == 'add':
        result = number1 + number2
    elif operation == 'subtract':
        result = number1 - number2
    else:
        error_message = "Operación no válida."
        return error_message

    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)

"""


from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculator', methods=['POST'])
def calculator():
    try:
        number1 = float(request.form['number1'])
        number2 = float(request.form['number2'])
        operation = request.form['operation']
    except ValueError:
        return "Invalid input for 'numero1' or 'numero2'", 400

    if operation == 'multiply':
        result = number1 * number2
    elif operation == 'divide':
        result = number1 / number2
    elif operation == 'add':
        result = number1 + number2
    elif operation == 'subtract':
        result = number1 - number2
    else:
        return "Invalid operation", 400

    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)
"""