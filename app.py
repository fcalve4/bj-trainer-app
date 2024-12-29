from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    game_state = "initial"
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

    # Add back cards
    card_images = ['back_dark.png', 'back_light.png']

    # Generate cards for each suit and rank
    for suit in suits:
        for rank in ranks:
            card_images.append(f"{suit}_{rank}.png")

    return render_template('index.html', game_state=game_state, card_images=card_images)


if __name__ == '__main__':
    app.run(debug=True)
