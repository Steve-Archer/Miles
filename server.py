from flask_app import app
from flask_app.controllers import locations, users


app.secret_key = "key"

if __name__ == '__main__':
    app.run(debug = True)