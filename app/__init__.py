from flask import Flask

# initializations
app = Flask(__name__)

# settings
app.secret_key = "mysecretkey"

# routes
from app import routes

# starting the app
if __name__ == "__main__":
    app.run()