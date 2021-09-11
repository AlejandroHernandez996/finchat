from flask import session, redirect, url_for, render_template, request
from app import app
from app.forms import QueryForm
from random_word import RandomWords

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = QueryForm()
    if form.validate_on_submit():
        ticker = form.query.data.upper()
        return redirect(url_for('.chat',query=ticker))
    return render_template('index.html',title='Home',form=form)
@app.route('/<query>')
def chat(query):
    ticker = query.upper()
    return render_template('chat.html',title='$'+ticker,ticker=ticker)

    
