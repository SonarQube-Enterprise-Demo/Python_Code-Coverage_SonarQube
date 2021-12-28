# app.py
from flask import Flask, request, render_template  # import flask

from models import Schema
from service import ToDoService

app = Flask(__name__)  # create an app instance


@app.route("/")  # at the end point /
def hello():  # call method hello
    # return "Hello World!"  # which returns "hello world"
    return render_template('index.html')


@app.route("/<name>")
def hello_name(name):
    return "Hello " + name


@app.route("/todo", methods=["POST"])
def create_todo():
    return ToDoService().create(request.get_json())

def add(e:int, f:int) -> int
    return e + f

def multiply(x: int, y: int) -> int:
    """multiply two numbers together

    Args:
                    x (int): first number in the multiplication
                    y (int): second number in the multiplication

    Returns:
                    int: product of x and y
    """
    return x * y

if __name__ == "__main__":  # on running python app.py
    Schema()
    app.run(debug=True)  # run the flask app
