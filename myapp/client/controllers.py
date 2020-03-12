from flask import Blueprint

client = Blueprint("client",__name__)

@client.route('/')
def index():
    return "Client"