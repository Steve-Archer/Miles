from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=["POST"])
def register():
    data = {
        'name': request.form['name']
    }
    if User.validate_user(data):
        User.register_user(data)
        flash('You are now registered. Please login')
        return redirect('/')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    if 'name' in session:
        session.clear()
    if 'name' not in session:
        session['name'] = ""
    data = {
        'name': request.form['name']
    }
    user_in_db = User.get_user(data)
    if not user_in_db:
        flash('Name not registered yet')
        return redirect('/')
    session['name'] = user_in_db.name
    print(session)
    return redirect('/start')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
