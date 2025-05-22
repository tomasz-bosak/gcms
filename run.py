from golf_app.app import create_app, db
from golf_app.app.models import Player, ScoreLog

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Player': Player, 'ScoreLog': ScoreLog}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
