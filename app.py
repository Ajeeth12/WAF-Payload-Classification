from flask import Flask, render_template, request
'''
It creates an instance of the Flask Class, which will be your WSGI (web server Gateway Interface) application.
'''

### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the Flask course</H1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello{name}!"
    return render_template('form.html')


@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


## Variable rule
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res="FAIL"

    return render_template('reult.html', results=res)

if __name__ == "__main__": # Entry point of the file
    app.run(debug=True)

