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
            'c':'+4.3223',
            'cp':'-0.12'
        }]
    elif code == 'goog':
        list = [{
            'l':'3,012.47',
            'c':'+3.4099',
            'cp':'-0.12'
        }]
    elif code == 'msft':
        list = [{
            'l':'5,322.37',
            'c':'+4.3225',
            'cp':'-0.12'
        }]
    elif code == 'fb':
        list = [{
            'l':'1,809.37',
            'c':'+3.3269',
            'cp':'-0.12'
        }]
    elif code == 'baba':
        list = [{
            'l':'8,327.37',
            'c':'+4.7655',
            'cp':'-0.12'
        }]
    response = jsonify(list)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=False)