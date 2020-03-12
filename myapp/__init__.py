from flask import Flask
from myapp.client.controllers import client
from myapp.user.controllers import user

app = Flask(__name__)

@app.route("/")
def index():
    return "HOmepagwe"


app.register_blueprint(client,url_prefix ="/")
app.register_blueprint(user,url_prefix ="/user")
