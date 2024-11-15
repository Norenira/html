from flask import Flask, request
import random
app = Flask(__name__)

@app.route("/hola")
def hello_world():
    return '<a href="/miRuta">Hello, World!</a>'

lista = [
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
    "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
    "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo.",
    "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
    "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"
]

@app.route("/miRuta")
def prueba():
    mensaje_aleatorio = random.choice(lista)
    return f'''
        <form action="/formulario" method="post">
            <input type="text" name="nombre" placeholder="Escribe tu nombre">
            <button type="submit">Enviar</button>
        </form>
        <form action="/lanzarMoneda" method="get">
            <button type="submit">Lanzar Moneda</button>
        </form>
        <p>{mensaje_aleatorio}</p>
    '''

@app.route("/formulario", methods=["post"])
def control():
    xd = request.form.get("nombre")
    return f"<h1>¡Hola, {xd}!</h1>"

@app.route("/lanzarMoneda", methods=["post"])
def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return f"<h1>Salió {resultado}!</h1>"


app.run(debug=True)
