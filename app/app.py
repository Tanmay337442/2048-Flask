from flask import Flask, render_template, request, jsonify, session
import logic

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

@app.route('/')
def index():
    session['data'] = logic.reset()
    return render_template('index.html', mat=session['data'][0], score=session['data'][1])

@app.route('/update-game', methods=['POST'])
def update():
    mat = session['data'][0]
    score = session['data'][1]
    key = request.json.get('key')
    if mat is not None and score is not None:
        next = logic.keys[key](mat)
        if next[0] != mat:
            mat, pts = logic.keys[key](mat)
            score += pts
            logic.addnum(mat)
            session['data'] = mat, score
        return jsonify({'mat': mat, 'score': score, 'state': logic.state(mat)})
    return "Not initialized"

if __name__ == '__main__':
    app.run(port=5000, debug=True)