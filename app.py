from flask import Flask

app: Flask = Flask(__name__)  # Crea el objeto Flask


@app.route('/')  # Usa la anotación para establecer la ruta
def home() -> str:  # Crea la función a correr en la ruta
    return '<h1>Hola Mundo</h1>'


# Correr la app para iniciar el server
app.run(host='localhost', port=8080, debug=True,)
