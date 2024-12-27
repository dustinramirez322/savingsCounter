from flask import Flask
import uuid
from routes import savings

app = Flask(__name__)
app.config['SECRET_KEY'] = uuid.uuid4().hex
app.register_blueprint(savings)

if __name__ == "__main__":
    app.run()
