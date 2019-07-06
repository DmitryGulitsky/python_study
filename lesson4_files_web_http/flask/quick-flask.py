from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index_page():
    names_list = ['John', 'Jim', 'Sara']
    return render_template('index.html', names=names_list)


@app.route('/hello/')
@app.route('/hello/<name>/')
def hello_page(name=None):
    #if not name is None:
    #    name = 'stranger'
    return render_template('hello.html', name =name)


# equal
#@app.route('/hello/<name>/')
#def hello_name(name):
#    return '<h3>Hello {name}</h3>'


@app.route('/article/')
@app.route('/article/int:<a_id>/')
def article_page(a_id=None):
    if a_id is None:
        return redirect(url_for('article_page', a_id=1))
    return render_template('article.html', a_id=a_id)


@app.route('/article/string:<a_id>/')
def article_page_str(a_id=None):
    return '<h1>Nothing for Article {a_id}</h1>', 404


@app.route('/user/', methods=['GET', 'POST'])
def user_page():
    print(request.form)
    if request.method == 'GET':
        return render_template('user.html')
    user_name = request.form.get('fname', 'not started')
    if not user_name:
        user_name = 'not stated'
    # error to debug
    1 / 0
    return f"<h3>USER NAME: {user_name}</h3>"


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)