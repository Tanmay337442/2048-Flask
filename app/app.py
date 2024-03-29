from flask import Flask, render_template, request, jsonify
import logic

app = Flask(__name__)

mat, score = [None, None]

@app.route('/')
def index():
    global mat, score
    mat, score = logic.reset()
    return render_template('index.html', mat=mat, score=score)

@app.route('/update-game', methods=['POST'])
def update():
    global mat, score
    key = request.json.get('key')
    if mat is not None and score is not None:
        next = logic.keys[key](mat)
        if next[0] != mat:
            mat, pts = logic.keys[key](mat)
            score += pts
            logic.addnum(mat)
        return jsonify({'mat': mat, 'score': score, 'state': logic.state(mat)})
    return "Not initialized"

if __name__ == '__main__':
    app.run(port=5000, debug=True)