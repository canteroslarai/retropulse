from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'retropulse_secret'

# Registro principal de 30 productos
PRODUCTOS = {i: {
    "id": i, 
    "nombre": f"Producto Retro {i}", 
    "precio": 5000 + (i * 100), 
    "descripcion": "Un artículo clásico de colección."
} for i in range(1, 31)}

@app.route('/')
def index():
    return render_template('index.html', productos=PRODUCTOS.values())

@app.route('/agregar/<int:id>', methods=['POST'])
def agregar(id):
    if 'carrito' not in session: session['carrito'] = []
    session['carrito'].append(PRODUCTOS[id])
    session.modified = True
    return redirect(url_for('ver_carrito'))

@app.route('/carrito')
def ver_carrito():
    items = session.get('carrito', [])
    total = sum(p['precio'] for p in items)
    return render_template('carrito.html', items=items, total=total)

if __name__ == '__main__':
    app.run(debug=True)