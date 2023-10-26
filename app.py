from flask import Flask, render_template, request

app = Flask(__name__)

def game_ran(difficulty=10):
    import random
    count = 10
    rand_num = random.randint(1, difficulty)
    while count != 0:
        try:
            g = int(request.form['guess'])
            if g == rand_num:
                return render_template('win.html', number=rand_num)
            elif g < rand_num:
                return render_template('guess_low.html', number=rand_num)
            elif g > rand_num:
                return render_template('guess_high.html', number=rand_num)
            count = count - 1
            return render_template('game.html', count=count)
        except ValueError:
            return render_template('error.html')
    else:
        return render_template('lose.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return game_ran(difficulty=int(request.form['difficulty']))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
