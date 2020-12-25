from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name = "hackathon", team_name = "THANH CUTE")

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
