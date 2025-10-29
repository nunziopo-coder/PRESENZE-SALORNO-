from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

presenze = []
print("Inizializzazione completata")

@app.route("/")
def index():
    # Passiamo direttamente il colore insieme a ogni presenza
    presenze_con_colore = []
    for p in presenze:
        colore = "green" if p["tipo"] == "Check-in" else "red"
        presenze_con_colore.append({**p, "colore": colore})
    return render_template("index.html", presenze=presenze_con_colore)

@app.route("/checkin", methods=["POST"])
def checkin():
    nome = request.form.get("nome")
    if nome:
        now = datetime.now()
        presenze.append({
            "nome": nome,
            "orario": now.strftime("%H:%M:%S"),
            "tipo": "Check-in",
            "data": now.strftime("%Y-%m-%d")
        })
    return redirect(url_for("index"))

@app.route("/checkout", methods=["POST"])
def checkout():
    nome = request.form.get("nome")
    if nome:
        now = datetime.now()
        presenze.append({
            "nome": nome,
            "orario": now.strftime("%H:%M:%S"),
            "tipo": "Check-out",
            "data": now.strftime("%Y-%m-%d")
        })
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
