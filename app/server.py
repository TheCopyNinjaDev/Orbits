from main import app


@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"
