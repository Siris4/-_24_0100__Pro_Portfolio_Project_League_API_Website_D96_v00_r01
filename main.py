from flask import Flask, render_template, request
from riot_api import get_summoner_id, get_live_game

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        summoner_name = request.form['summoner_name']
        region = 'na1'  # Set your default region here, or allow user input for region

        # Get the summoner ID using the summoner name
        summoner_id = get_summoner_id(summoner_name, region)
        if not summoner_id:
            return render_template('index.html', error="Summoner not found!")

        # Get live game data if the summoner is in a match
        live_game_data = get_live_game(summoner_id, region)
        if live_game_data:
            participants = live_game_data['participants']
            game_queue_id = live_game_data['gameQueueConfigId']
            is_aram = (game_queue_id == 450)

            return render_template('index.html', participants=participants, is_aram=is_aram)
        else:
            return render_template('index.html', error="Summoner is not in an active game.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
