from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Sample Api Project!'

@app.route('/api')
def api():
    return {'message': 'This is my API endpoint'}

if __name__ == '__main__':
    app.run(debug=True)
