from flask import Flask, session, render_template, redirect
from flask.templating import render_template
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'col3'

boggle_game = Boggle()

@app.route('/')
def home_page():

    board = boggle_game.make_board()
    session['board'] = board

    return render_template('base.html', board = board)

