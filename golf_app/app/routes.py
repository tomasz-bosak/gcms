from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import Player, ScoreLog

main = Blueprint('main', __name__)

@main.route('/add_player', methods=['POST'])
def add_player():
    player_name = request.form.get('player_name')
    if player_name:
        existing_player = Player.query.filter_by(name=player_name).first()
        if not existing_player:
            # Default new player to hole 1, score 0
            new_player = Player(name=player_name, current_hole=1, current_score=0)
            db.session.add(new_player)
            db.session.commit()
            flash(f'Player {player_name} added successfully!', 'success')
        else:
            flash(f'Player {player_name} already exists.', 'warning')
    else:
        flash('Player name cannot be empty.', 'error')
    return redirect(url_for('main.overview'))

@main.route('/', methods=['GET'])
def overview():
    players = Player.query.all()
    # The template 'overview.html' will be created in a later step.
    return render_template('overview.html', players=players)

@main.route('/tee/<int:hole_number>', methods=['GET', 'POST'])
def tee_box(hole_number):
    if request.method == 'POST':
        player_name = request.form.get('player_name')
        score_value = request.form.get('score_value')
        previous_hole_str = request.form.get('previous_hole') # Expected to be hole_number - 1

        player = Player.query.filter_by(name=player_name).first()

        if player and score_value and previous_hole_str:
            # As per simplified instructions, directly convert and assume valid inputs
            score = int(score_value)
            previous_hole = int(previous_hole_str)

            log = ScoreLog(player_id=player.id, hole_number=previous_hole, score=score)
            db.session.add(log)
            
            # Initialize current_score if None, then increment
            if player.current_score is None:
                player.current_score = 0
            player.current_score += score
            
            player.current_hole = hole_number 
            
            db.session.commit()
            flash(f'Score for {player.name} on hole {previous_hole} recorded!')
        else:
            flash('Error recording score. Check inputs.')
        
        return redirect(url_for('main.tee_box', hole_number=hole_number))

    # GET request
    players = Player.query.all() # To populate player selection in the form
    # Pass current players for the form, and the current hole_number for display
    return render_template('tee_box.html', hole_number=hole_number, players=players)

@main.route('/record_score', methods=['POST'])
def record_score_route():
    # This route is placeholder as per instructions
    flash("Score recorded (placeholder from /record_score). This route might be deprecated.")
    return redirect(url_for('main.overview'))
