from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        number = request.form['number']
        try:
            response = requests.get(f'http://app-b:5001/evaluate/{number}')
            result = response.text
        except requests.exceptions.RequestException as e:
            result = f"Error: {str(e)}"
    return render_template('form.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
