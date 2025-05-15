from flask import Flask

app = Flask(__name__)

@app.route('/evaluate/<int:number>')
def evaluate(number):
    result = "par" if number % 2 == 0 else "impar"
    return f"{number} es {result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
