from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def head():
    return render_template("index.html", number1=49, number2=66)

@app.route("/sum")
def number():
    num1, num2 = 23, 89
    return render_template("body.html", value1=num1, value2=num2, sum=num1+num2)



if __name__== "__main__":
#   app.run(debug=True)

   app.run(host='0.0.0.0', port=80) # to run on the EC2-instance, please non-comment this line.  