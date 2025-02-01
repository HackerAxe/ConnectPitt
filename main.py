from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')
    
    return redirect(url_for('results'))

@app.route("/results")
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)