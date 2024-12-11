from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<a href="/theroute">Hello, World!</a> <br> <a href="/funfact">Un dato curioso...</a> <br> <a href="/hidden">La página oculta</a>'

@app.route("/theroute")
def functional():
    return '<hi>Qué tal!</h1>'

@app.route("/funfact")
def fun_fact():
    return '<h1>¿Sabías que hay una planta llamada "Welwitschia mirabilis" que se encuentra en el desierto de Namibia y Angola? Esta planta es notable por su longevidad y resistencia, ya que puede vivir hasta 2,000 años o más con solo dos hojas que crecen continuamente a lo largo de su vida. Es una de las plantas más resistentes y antiguas del mundo. 🌵🌟</h1>'

@app.route("/hidden")
def oculto():
    return '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAsXb2ywro-gnQtbSSYD5KENBBH2lk0DIqjA&s"alt>'
app.run(debug=True)
