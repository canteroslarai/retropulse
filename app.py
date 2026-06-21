from flask import Flask, render_template

app = Flask(__name__)

# Lista completa de 15 productos
productos = [
    {'id': 1, 'nombre': 'Cámara Kodak Vintage', 'precio': 35.5, 'tipo': 'Coleccionable'},
    {'id': 2, 'nombre': 'Consola Retro 8-bit', 'precio': 51.0, 'tipo': 'Tecnología'},
    {'id': 3, 'nombre': 'Vinilo de Jazz 1960', 'precio': 66.5, 'tipo': 'Coleccionable'},
    {'id': 4, 'nombre': 'Walkman Sony Original', 'precio': 82.0, 'tipo': 'Tecnología'},
    {'id': 5, 'nombre': 'Teléfono de Disco', 'precio': 97.5, 'tipo': 'Coleccionable'},
    {'id': 6, 'nombre': 'Calculadora Casio Retro', 'precio': 113.0, 'tipo': 'Tecnología'},
    {'id': 7, 'nombre': 'Reloj de Bolsillo', 'precio': 128.5, 'tipo': 'Coleccionable'},
    {'id': 8, 'nombre': 'Joystick Arcade', 'precio': 144.0, 'tipo': 'Tecnología'},
    {'id': 9, 'nombre': 'Posters Vintage', 'precio': 159.5, 'tipo': 'Coleccionable'},
    {'id': 10, 'nombre': 'Radio Transistor', 'precio': 175.0, 'tipo': 'Tecnología'},
    {'id': 11, 'nombre': 'Máquina de escribir', 'precio': 190.5, 'tipo': 'Coleccionable'},
    {'id': 12, 'nombre': 'Monitor CRT Retro', 'precio': 206.0, 'tipo': 'Tecnología'},
    {'id': 13, 'nombre': 'Lámpara Art Deco', 'precio': 221.5, 'tipo': 'Coleccionable'},
    {'id': 14, 'nombre': 'Teclado Mecánico Retro', 'precio': 237.0, 'tipo': 'Tecnología'},
    {'id': 15, 'nombre': 'Juego de mesa 1970', 'precio': 252.5, 'tipo': 'Coleccionable'}
]

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)