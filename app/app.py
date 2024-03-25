from flask import Flask, render_template, request, jsonify
import game

app = Flask(__name__)

mat, score = [None, None]

@app.route('/')
def index():
    global mat, score
    mat, score = game.reset()
    return render_template('index.html', mat=mat, score=score)

@app.route('/update-game', methods=['POST'])
def update():
    global mat, score
    key = request.json.get('key')
    if mat is not None and score is not None:
        next = game.keys[key](mat)
        if next[0] != mat:
            mat, pts = game.keys[key](mat)
            score += pts
            game.addnum(mat)
        return jsonify({'mat': mat, 'score': score, 'state': game.state(mat)})
    return "Not initialized"

if __name__ == '__main__':
    app.run(port=8000, debug=True)