
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/imc", methods = ['GET','POST'])
def calcular_imc():
    nome = None
    massa = None
    altura = None
    imc = None
    diagnostico = None
    result = ""
    if request.method == "POST":
        nome = request.form.get("nome","")
        massa = float(request.form.get("massa","").replace(",","."))
        altura = float(request.form.get("altura","").replace(",","."))
        imc = massa/(altura**2)

        if imc < 18.5:
            diagnostico = "Você está abaixo do peso ideal"
        elif imc < 25:
            diagnostico = "Você está no peso ideal"
        elif imc < 30:
            diagnostico = "Você está acima do peso ideal"
        elif imc < 35:
            diagnostico = "Você está obeso"
        elif imc < 40:
            diagnostico = "Você está com obesidade nivel 2"
        else:
            diagnostico = "Você está com obesidade morbida"
            
        result = f"{nome}, seu IMC é {imc:.2f}."

    return render_template("index.html", result=result, diagnostico = diagnostico)


if __name__ == "__main__":
    app.run(debug=True)