from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "/Chastain/index.html"

if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)
    
