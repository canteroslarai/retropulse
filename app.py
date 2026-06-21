from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'retropulse_secret_2026'

# Base de datos de 15 productos
PRODUCTOS = {i: {"id": i, "nombre": f"Producto Retro {i}", "precio": i * 5000, "desc": "Hardware premium con estética clásica y alta durabilidad."} for i in range(1, 16)}

@app.route('/')
def index():
    return render_template('index.html', productos=PRODUCTOS.values())

@app.route('/detalle/<int:id>')
def detalle(id):
    producto = PRODUCTOS.get(id)
    return render_template('detalle.html', producto=producto)

@app.route('/agregar/<int:id>', methods=['POST'])
def agregar(id):
    c = session.get('carrito', {})
    c[str(id)] = c.get(str(id), 0) + 1
    session['carrito'] = c
    return redirect(url_for('index'))

@app.route('/carrito')
def carrito():
    items = []
    total = 0
    for id, cant in session.get('carrito', {}).items():
        p = PRODUCTOS[int(id)]
        items.append({**p, 'cant': cant})
        total += p['precio'] * cant
    return render_template('carrito.html', items=items, total=total)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)