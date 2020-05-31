from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Stay inside, stay safe and keep social distancing."

if __name__ == '__main__':
 app.run(debug=True,host='0.0.0.0',port=5000)
app.run(host='0.0.0.0') 
