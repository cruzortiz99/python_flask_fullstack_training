from flask import Flask, request, url_for, redirect, render_template
from werkzeug.wrappers import Response
from werkzeug.exceptions import NotFound
from typing import Optional, Union, List, Tuple, Any


# Crea el objeto Flask, se puede definir la carpeta para ubicar los templates
app: Flask = Flask(__name__)


@app.route('/')  # Usa la anotación para establecer la ruta
def home() -> str:  # Crea la función a correr en la ruta
    return render_template('index.html')  # Usando template


@app.route('/user')  # Se pueden obtener los parámetros/query de la app
def params() -> Union[Response, str]:
    # a través del uso de request de flask y el nombre esperado
    name: Optional[str] = request.args.get('name')
    # Los parametros/query se concatenan con &
    last_name: Optional[str] = request.args.get('last-name')
    age: Optional[int] = request.args.get('age')
    list: List[str] = ['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco']
    if name is not None and last_name is not None and age is not None:
        return render_template(
            'user.html',
            name=name.capitalize(),
            last_name=last_name.capitalize(),
            age=int(age),
            list=list)
    else:
        return redirect('/')

# Una función puede estar asignada a diferentes rutas
@app.route('/variable-default')
# Se pueden obtener rutas dinámicas al crear variables en las rutas
# Se le puede especificar el parser del valor de la ruta directamente a la ruta
@app.route('/variable/<name>/<int:value>')
def path_variable(name: str = 'default', value: int = 0) -> str:
    return f'El nombre de la variable es: {name}, y su valor es {value}'


@app.errorhandler(404)  # Manejando error 404 en flask
def page_not_found(error: NotFound) -> Tuple[str, int]:
    return render_template('404.html'), 404  # Se manda una tuple con el error


# Correr la app para iniciar el server
if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True,)
# debug mantiene el servidor vivo para que recargue la app
