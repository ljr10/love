from flask import Flask

app = Flask(__name__)

@app.route('/')
def love():
    return "아빠 사랑해"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5733)
