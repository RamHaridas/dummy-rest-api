from flask import Flask, render_template,send_file
from flask_assets import Bundle, Environment
from flask_restful import Api
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import psycopg2
import os

# normal url for database should be saved as an environment variable
# when used for production
normal = os.environ.get('MY_DATABASE_URL')

postgres_url = {
    'user': 'ram',
    'pw': 'ram',
    'db': 'dummy',
    'host': 'localhost',
    'port': '5432',
}

local_url = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % postgres_url

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = local_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)


# ADD ENDPOINTS HERE
# api.add_resource(ResurceClassName,'/endpoint')



# CORS ENABLING FOR ANGULAR/REACT FRONT END
# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers',
#                          'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods',
#                          'GET,PUT,POST,DELETE,PATCH')
#     return response



@app.before_first_request
def create_tables():
    db.create_all()

# MAIN FUNCTION
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    # migrate  = Migrate(app, db)
    # manager = Manager(app)
    # manager.add_command('db', MigrateCommand)
    # manager.run()
    app.run(port=5000, debug=True)
