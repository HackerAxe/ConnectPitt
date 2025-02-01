from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/results")
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)