from flask import request, Flask

app = Flask(__name__)

@app.route('/')
def home():
    h = request.headers
    print(h)
    return "Hi"

app.run()
