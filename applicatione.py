from flask import Flask
from flask_cors import CORS

from database import setup
from resources.tasks import register_bp, product_bp, login_bp,logout_bp

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
setup.create_tables()


@app.before_first_request
def create_tables():
    setup.create_tables()


app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(product_bp)

if __name__ == '__main__':
    app.run(debug=True)
