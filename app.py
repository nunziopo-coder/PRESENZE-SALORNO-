from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Inizializzazione dati all'avvio
presenze = []
print("Inizializzazione completata")  # Qui prima c'era before_first_request / before_serving

@app.route("/")
def index():
    return render_template("index.html", presenze=presenze)

@app.route("/checkin", methods=["POST"])
def checkin():
    nome = request.form.get("nome")
    if nome:
        presenze.append({"nome": nome, "orario": datetime.now().strftime("%H:%M:%S"), "tipo": "Check-in"})
    return redirect(url_for("index"))

@app.route("/checkout", methods=["POST"])
def checkout():
    nome = request.form.get("nome")
    if nome:
        presenze.append({"nome": nome, "orario": datetime.now().strftime("%H:%M:%S"), "tipo": "Check-out"})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
