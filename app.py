from flask import Flask
from routes import curriculum_blueprint
from flask_migrate import Migrate
from flask_login import LoginManager
import models
from models import init_app

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yUP5UTCMXFA2pdaDusVJsz'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///./database/curriculums.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
models.init_app(app)

app.register_blueprint(curriculum_blueprint)
login_manager = LoginManager(app)
migrate = Migrate(app, models.db)

if __name__ == '__main__':
    app.run(debug=True, port=5004)