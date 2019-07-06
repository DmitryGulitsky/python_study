from flask import Flask, render_tmplate

app = Flask(__name__)


@app.route('/')
def index_page():
    names_list = ['John', 'Jim', 'Sara']
    return render_template('index.html', names=names_list)


@app.route('/hello/')
@app.route('/hello/<name>/')
def hello_page(name=None):
    if name is None:
        name = 'Page'
    return '<h2>Hello {name}!</h2>'


# equal
#@app.route('/hello/<name>/')
#def hello_name(name):
#    return '<h3>Hello {name}</h3>'

if __name__ == '__main__':
    app.run(host='localhost', port=5000)