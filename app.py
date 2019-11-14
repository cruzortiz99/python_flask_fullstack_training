from flask import Flask, request
from typing import Optional

app: Flask = Flask(__name__)  # Crea el objeto Flask


@app.route('/')  # Usa la anotación para establecer la ruta
def home() -> str:  # Crea la función a correr en la ruta
    return '<h1>Hola Mundo</h1>'


@app.route('/params')  # Se pueden obtener los parámetros/query de la app
def params() -> str:
    # a través del uso de request de flask y el nombre esperado
    name: Optional[str] = request.args.get('name')
    # Los parametros/query se concatenan con &
    last_name: Optional[str] = request.args.get('last-name')
    return f'Tu nombre es: {name} {last_name}'

# Una función puede estar asignada a diferentes rutas
@app.route('/variable-default')
# Se pueden obtener rutas dinámicas al crear variables en las rutas
# Se le puede especificar el parser del valor de la ruta directamente a la ruta
@app.route('/variable/<name>/<int:value>')
def path_variable(name: str = 'default', value: int = 0) -> str:
    return f'El nombre de la variable es: {name}, y su valor es {value}'


# Correr la app para iniciar el server
if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True,)
# debug mantiene el servidor vivo para que recargue la app
