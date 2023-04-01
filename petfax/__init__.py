from flask import Flask 
from flask_migrate import Migrate

#this would be considered our factory method
def create_app(): 
    app = Flask(__name__)

    #database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
    
    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'
    
    #registering the Pet Blueprint
    from . import pet 
    app.register_blueprint(pet.bp)

    #registering the facts blueprint
    from . import fact
    app.register_blueprint(fact.bp)
    
    return app

