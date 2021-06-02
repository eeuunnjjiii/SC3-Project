from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234@localhost:3306/project?charset=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #orm 연결
    db.init_app(app)

    #migrate 연결
    migrate.init_app(app, db)
    
    from sc3.routes import brand_route
    app.register_blueprint(brand_route.bp)

    from sc3.routes import main_route
    app.register_blueprint(main_route.bp)

    from sc3.routes import company_route
    app.register_blueprint(company_route.bp)

    from sc3.routes import industry_route
    app.register_blueprint(industry_route.bp)
    
    from sc3.routes import check_route
    app.register_blueprint(check_route.bp)

    from sc3.routes import predict_route
    app.register_blueprint(predict_route.bp)

    return app



if __name__ == "__main__":
    app = create_app()
    app.run()