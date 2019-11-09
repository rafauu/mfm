from flask import Flask, render_template, request

app = Flask(__name__)

name = "first"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def index2():
    global name
    name = request.get_json()['name']
    print(name)
    return ""

@app.route('/getName')
def index3():
    global name
    print(name)
    #name = name + "1"
    return name

if __name__ == '__main__':
    app.run(debug=True)
