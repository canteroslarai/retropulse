import os
from flask import Flask, render_template, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'retropulse_secret_key_2026'

# Catálogo completo de 15 productos con imágenes URL de marcadores temáticos
PRODUCTOS = {
    1: {"id": 1, "nombre": "Consola Retro Classic X", "precio": 45000, "descripcion": "Consola con más de 10.000 juegos clásicos de los 90. Incluye dos mandos inalámbricos y conexión HDMI.", "imagen": "https://images.unsplash.com/photo-1531525645387-7f14be1bdbbd?w=500&auto=format&fit=crop&q=60"},
    2: {"id": 2, "nombre": "Gamepad Pro Wireless", "precio": 18000, "descripcion": "Control inalámbrico ergonómico de alta precisión compatible con PC, Android y consolas retro.", "imagen": "https://images.unsplash.com/photo-1592840496694-26d035b52b48?w=500&auto=format&fit=crop&q=60"},
    3: {"id": 3, "nombre": "Cartucho Legendario 99-en-1", "precio": 12000, "descripcion": "El mítico cartucho con los mejores éxitos de la época dorada de los videojuegos de 8 y 16 bits.", "imagen": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=500&auto=format&fit=crop&q=60"},
    4: {"id": 4, "nombre": "Consola Portátil Pocket", "precio": 35000, "descripcion": "Pantalla IPS de 3.5 pulgadas para llevar tus emuladores favoritos (GameBoy, Megadrive) a todos lados.", "imagen": "https://images.unsplash.com/photo-1546776310-eef45dd6d63c?w=500&auto=format&fit=crop&q=60"},
    5: {"id": 5, "nombre": "Lámpara LED Pac-Man Pixel", "precio": 9500, "descripcion": "Lámpara decorativa pixelada con modo sensible al sonido que reacciona al ritmo de tu música.", "imagen": "https://images.unsplash.com/photo-1563089145-599997674d42?w=500&auto=format&fit=crop&q=60"},
    6: {"id": 6, "nombre": "Llavero Metálico Arcade", "precio": 2500, "descripcion": "Llavero premium de metal con la forma detallada de una máquina de fichines clásica de los 80.", "imagen": "https://images.unsplash.com/photo-1589254065878-42c9da997008?w=500&auto=format&fit=crop&q=60"},
    7: {"id": 7, "nombre": "Mouse Pad Gamer Retro", "precio": 7500, "descripcion": "Mouse pad tamaño extra largo con diseño retro-wave ideal para setup de diseño o gaming.", "imagen": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=500&auto=format&fit=crop&q=60"},
    8: {"id": 8, "nombre": "Auriculares Retro Sound", "precio": 22000, "descripcion": "Auriculares con estética de los 80 pero tecnología moderna: Bluetooth 5.0 y cancelación de ruido.", "imagen": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&auto=format&fit=crop&q=60"},
    9: {"id": 9, "nombre": "Gorra RetroPulse Classic", "precio": 6000, "descripcion": "Gorra estilo trucker con el logotipo oficial de RetroPulse bordado en alta definición.", "imagen": "https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=500&auto=format&fit=crop&q=60"},
    10: {"id": 10, "nombre": "Remera Algodón Pixel Art", "precio": 14000, "descripcion": "Remera 100% algodón con estampa premium de estética pixel art y colores vibrantes de larga duración.", "imagen": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=500&auto=format&fit=crop&q=60"},
    11: {"id": 11, "nombre": "Taza Cerámica Game Over", "precio": 4800, "descripcion": "Taza de cerámica importada con diseño termosensible que cambia de color al agregar líquido caliente.", "imagen": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=500&auto=format&fit=crop&q=60"},
    12: {"id": 12, "nombre": "Consola Mini Arcade Bartop", "precio": 85000, "descripcion": "Réplica a escala de una máquina arcade para mesa. Pantalla integrada y palanca clásica de alta respuesta.", "imagen": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=500&auto=format&fit=crop&q=60"},
    13: {"id": 13, "nombre": "Cable HDMI Mallado Premium", "precio": 3500, "descripcion": "Cable HDMI de alta velocidad con conector dorado y protección mallada para evitar interferencias.", "imagen": "https://images.unsplash.com/photo-1557672172-298e090bd0f1?w=500&auto=format&fit=crop&q=60"},
    14: {"id": 14, "nombre": "Kit Limpieza Consolas", "precio": 5500, "descripcion": "Kit especializado con alcohol isopropílico, cepillos antiestáticos y paño para mantener tus joyas retro impecables.", "imagen": "https://images.unsplash.com/photo-1581092921461-eab62e97a780?w=500&auto=format&fit=crop&q=60"},
    15: {"id": 15, "nombre": "Póster Neón Cyberpunk", "precio": 3800, "descripcion": "Póster satinado tamaño A3 con diseño retro-futurista e impresión de alta calidad para decorar tu habitación.", "imagen": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=500&auto=format&fit=crop&q=60"}
}

@app.route('/')
def index():
    return render_template('index.html', productos=PRODUCTOS.values())

@app.route('/producto/<int:id_producto>')
def detalle(id_producto):
    producto = PRODUCTOS.get(id_producto)
    if not producto:
        flash("Producto no encontrado", "error")
        return redirect(url_for('index'))
    return render_template('detalle.html', producto=producto)

@app.route('/agregar/<int:id_producto>', methods=['POST'])
def agregar_al_carrito(id_producto):
    producto = PRODUCTOS.get(id_producto)
    if producto:
        if 'carrito' not in session:
            session['carrito'] = []
        
        carrito = session['carrito']
        carrito.append({
            "id": producto["id"],
            "nombre": producto["nombre"],
            "precio": producto["precio"]
        })
        session['carrito'] = carrito
        flash(f"{producto['nombre']} añadido.", "success")
    return redirect(url_for('index'))

@app.route('/carrito')
def ver_carrito():
    items = session.get('carrito', [])
    total = sum(item['precio'] for item in items)
    return render_template('carrito.html', items=items, total=total)

@app.route('/limpiar')
def limpiar_carrito():
    session.pop('carrito', None)
    return redirect(url_for('ver_carrito'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)