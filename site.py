from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route('/Contatos')
def Contatos():
    return render_template('contatos.html')


if __name__ == "__main__":
    app.run(debug=True)


