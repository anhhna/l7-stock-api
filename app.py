from flask import Flask, jsonify, render_template

# App Globals (do not edit)
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/stock/<code>')
def stock(code):
    list = []
    if code == 'appl':
        list = [{
            'l':'4,022.37',
            'c':'+3.3269',
            'id':'-0.12'
        }]
    elif code == 'goog':
        list = [{
            'l':'4,022.37',
            'c':'+3.3269',
            'id':'-0.12'
        }]
    elif code == 'msft':
        list = [{
            'l':'4,022.37',
            'c':'+3.3269',
            'id':'-0.12'
        }]
    elif code == 'fb':
        list = [{
            'l':'4,022.37',
            'c':'+3.3269',
            'id':'-0.12'
        }]
    elif code == 'baba':
        list = [{
            'l':'4,022.37',
            'c':'+3.3269',
            'id':'-0.12'
        }]
    return jsonify(list)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=False)