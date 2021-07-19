from flask import Flask

app = Flask("api_test")

@app.route('/')
def hello():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)