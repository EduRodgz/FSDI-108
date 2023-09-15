from flask import Flask
from config import developer
import json

app = Flask("server")

@app.get("/")
def hello():
    return "Hello from Flask"

@app.get("/test")
def test():
    return "I am a page"

@app.get("/name")
def name():
    return "Eduardo Rodriguez"





#products API

@app.get("/api/about")
def about_me():
    return json.dumps(developer)

@app.get("/api/products")
def get_products():
    products = []

    return json.dumps(products)

app.run(debug = True)