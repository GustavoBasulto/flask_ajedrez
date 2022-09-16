from flask import Flask, render_template 
app = Flask(__name__)    

@app.route('/')                           
def inicio():
    return render_template('index.html', num1=8, num2=8)

@app.route('/<int:num1>')                           
def number(num1):
    return render_template('index.html', num1=num1, num2=8)

@app.route('/<int:num1>/<int:num2>')                           
def number2(num1, num2):
    return render_template('index.html', num1=num1, num2=num2)

@app.route('/<int:num1>/<int:num2>/<string:col1>/<string:col2>')                           
def numberycolor(num1, num2, col1, col2):
    return render_template('index.html', num1=num1, num2=num2, col1=col1, col2=col2)



@app.route('/play/<int:num>/<string:color>')                           
def playc(num,color):
    return render_template('index.html', num=num, color=color) 
    
if __name__=="__main__":
    app.run(debug=True)   