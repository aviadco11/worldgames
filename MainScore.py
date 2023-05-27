import Utils
from flask import Flask

app = Flask("World of Games - MainScores")


@app.route('/')
def score_server():
    try:
        my_file = open(Utils.SCORES_FILE_NAME, "r", encoding="utf-8")
        for line in my_file.readlines():
            score = (int(line))
        output = '<html><head><title>Scores Game</title></head><body><h1>The score is <div id="score">{0}</div></h1></body></html>'.format(score)
    except BaseException as e:
        output = '<html><head><title>Scores Game</title></head><body><body><h1><div id="score" style="color:red">{0}</div></h1>'.format(e.error)
    finally:
        return output

app.run(host="0.0.0.0", port=5001, debug=False)
