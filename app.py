from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'retropulse_secret_2026'

# Generador de 30 productos para no escribir 1000 líneas
CATEGORIAS = ["Consolas", "Accesorios", "Ropa", "Decoración"]
PRODUCTOS = [{
    "id": i, "nombre": f"Producto Retro {i}", "precio": (i % 5 + 1) * 5000,
    "cat": CATEGORIAS[i % 4], "img": f"https://picsum.photos/id/{i+10}/300/300",
    "desc": "Hardware premium con estética clásica y alta durabilidad."
} for i in range(1, 31)]

@app.route('/')
def index():
    return render_template('index.html', destacados=PRODUCTOS[:4])

@app.route('/tienda')
def tienda():
    cat = request.args.get('cat')
    lista = [p for p in PRODUCTOS if p['cat'] == cat] if cat else PRODUCTOS
    return render_template('tienda.html', productos=lista)

@app.route('/producto/<int:id>')
def producto(id):
    p = next((x for x in PRODUCTOS if x['id'] == id), None)
    return render_template('producto.html', p=p)

@app.route('/carrito', methods=['GET', 'POST'])
def carrito():
    if request.method == 'POST':
        id = request.form.get('id')
        c = session.get('carrito', {})
        c[id] = c.get(id, 0) + 1
        session['carrito'] = c
    items = []
    total = 0
    for id, cant in session.get('carrito', {}).items():
        p = next(x for x in PRODUCTOS if x['id'] == int(id))
        items.append({**p, 'cant': cant})
        total += p['precio'] * cant
    return render_template('carrito.html', items=items, total=total)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        session.pop('carrito', None)
        return "<h1>¡Gracias por tu compra! Tu pedido está en camino.</h1><a href='/'>Volver al inicio</a>"
    return render_template('checkout.html')

import os

if __name__ == '__main__':
    # Render asigna automáticamente un puerto dinámico en la variable de entorno PORT
    port = int(os.environ.get("PORT", 5000))
    # '0.0.0.0' le dice a Flask que sea accesible externamente
    app.run(host="0.0.0.0", port=port)