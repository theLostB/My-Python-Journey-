from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask on Pydroid!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8181)
