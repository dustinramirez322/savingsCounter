from flask import Flask
import uuid

app = Flask(__name__)

app.config['SECRET_KEY'] = uuid.uuid4().hex

from app import routes

if __name__ == "__main__":
    app.run(debug=True)
