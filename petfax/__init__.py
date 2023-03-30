from flask import Flask 
#this would be considered our factory method
def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'
    
    #registering the Pet Blueprint
    from . import pet 
    app.register_blueprint(pet.bp)

    return app
