from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.location import Location
from flask_app.models.user import User
import random


@app.route('/start')
def game():
    if 'score' in session:
        session['score'].clear()
    if 'round' in session:
        session['round'].clear()
    if 'name' not in session:
        flash('please login')
        return redirect('/')
    return render_template('start.html')

@app.route('/play')
def play():
    if 'name' not in session:
        flash('please login')
        return redirect('/')
    if 'round' in session:
        session['round'] += 1
    if 'round' not in session:
        session['round'] = 1
    if 'score' not in session:
        session['score'] = 0
    if session['round'] == 11:
        return redirect('/end_game')
    num = random.sample(range(1, 101), 2)
    num1 = num[0]
    num2 = num[1]
    round = session['round'] 
    dataOne = {
        'id': num1
    }
    dataTwo = {
        'id': num2
    }
    print(num1)
    cityOne = Location.get_city(dataOne)
    cityTwo = Location.get_city(dataTwo)
    print(cityOne)
    return render_template('game.html', cityOne=cityOne, cityTwo=cityTwo, round=round)

@app.route('/new_round', methods=['POST'])
def round_end():
    score = int(request.form['score'])
    session_score = session['score']
    score += int(session_score)
    session['score'] = score
    return redirect ('/play')

@app.route('/end_game')
def end_game():
    data = {
        'name': session['name'],
    }
    score = User.get_score(data)
    new_data = {
            'name': session['name'],
            'score': session['score']
        }
    if score[0]['score'] > session['score']:
        User.new_score(new_data)
    users = User.get_best_scores()
    print(users)
    return render_template('end.html', users=users)

@app.route('/play_again')
def play_again():
    user = session['name']
    session.clear()
    if 'name' not in session:
        session['name'] = user
    return redirect('/start')