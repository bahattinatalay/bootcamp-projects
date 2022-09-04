from flask import Flask 

app = Flask(__name__)

@app.route("/")
def head():
    return "<h1> <p>Hello World! </p>  This is the start page. </h1>"


@app.route("/second")
def second():
    return "<h2>This is my second page</h2>"

@app.route("/third/sub3")
def third():
    return "<h2>This is the subpath of third page</h2>"

@app.route("/fourth/<string:id>")
def fourth(id):
    return f'Id of this page is {id}'


if __name__ == "__main__":
#   app.run(debug=True)

    app.run(host='0.0.0.0', port=80) # to run on the EC2-instance, please non-comment this line.    