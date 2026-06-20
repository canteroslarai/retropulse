from flask import Flask, render_template

app = Flask(__name__)

# Nuestra "Base de Datos" con 15 productos vintage y retro
lista_productos = [
    {
        "id_producto": "RETRO-001",
        "nombre": "Game Boy Color (Berry)",
        "categoria": "Consolas",
        "anio_fabricacion": 1998,
        "estado_conservacion": "Como nuevo (Mint)",
        "precio": 120.00,
        "stock": 1,
        "descripcion": "Consola portátil original en edición Berry. Limpieza interna completa.",
        "imagen_url": "https://images.unsplash.com/photo-1531525645387-7f14be1bdbbd?w=400"
    },
    {
        "id_producto": "RETRO-002",
        "nombre": "Cámara Polaroid Sun 600",
        "categoria": "Fotografía",
        "anio_fabricacion": 1983,
        "estado_conservacion": "Buen estado",
        "precio": 85.00,
        "stock": 1,
        "descripcion": "Cámara instantánea clásica. Probada y funcionando con cartuchos e-600.",
        "imagen_url": "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400"
    },
    {
        "id_producto": "RETRO-003",
        "nombre": "Vinilo Michael Jackson - Thriller",
        "categoria": "Música",
        "anio_fabricacion": 1982,
        "estado_conservacion": "Excelente (VG+)",
        "precio": 45.00,
        "stock": 2,
        "descripcion": "Primera edición estadounidense. Incluye el insert original con letras.",
        "imagen_url": "https://images.unsplash.com/photo-1603048588665-791ca8aea617?w=400"
    },
    {
        "id_producto": "RETRO-004",
        "nombre": "Sega Genesis / Mega Drive",
        "categoria": "Consolas",
        "anio_fabricacion": 1989,
        "estado_conservacion": "Detalles estéticos",
        "precio": 95.00,
        "stock": 1,
        "descripcion": "Modelo 1 original. Incluye transformador, cable RCA y un joystick de 3 botones.",
        "imagen_url": "https://images.unsplash.com/photo-1612036782180-6f0b6cd846fe?w=400"
    },
    {
        "id_producto": "RETRO-005",
        "nombre": "Walkman Sony WM-F22",
        "categoria": "Audio",
        "anio_fabricacion": 1986,
        "estado_conservacion": "Para repuestos",
        "precio": 30.00,
        "stock": 1,
        "descripcion": "Estéticamente hermoso pero requiere cambio de correas internas. No reproduce.",
        "imagen_url": "https://images.unsplash.com/photo-1611002214175-92576b92a2a1?w=400"
    },
    {
        "id_producto": "RETRO-006",
        "nombre": "Cartucho Super Mario World (SNES)",
        "categoria": "Videojuegos",
        "anio_fabricacion": 1990,
        "estado_conservacion": "Buen estado",
        "precio": 40.00,
        "stock": 3,
        "descripcion": "Cartucho original para Super Nintendo. Placa limpia y contactos pulidos.",
        "imagen_url": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400"
    },
    {
        "id_producto": "RETRO-007",
        "nombre": "Computadora Commodore 64",
        "categoria": "Computación",
        "anio_fabricacion": 1982,
        "estado_conservacion": "Como nuevo (Mint)",
        "precio": 250.00,
        "stock": 1,
        "descripcion": "En caja original con manuales. Una pieza de museo perfectamente funcional.",
        "imagen_url": "https://images.unsplash.com/photo-1547082299-de196ea013d6?w=400"
    },
    {
        "id_producto": "RETRO-008",
        "nombre": "Consola Nintendo NES",
        "categoria": "Consolas",
        "anio_fabricacion": 1985,
        "estado_conservacion": "Buen estado",
        "precio": 130.00,
        "stock": 1,
        "descripcion": "Lanzamiento americano. Mantenimiento de pinera de 72 pines recién hecho.",
        "imagen_url": "https://images.unsplash.com/photo-1531525645387-7f14be1bdbbd?w=400"
    },
    {
        "id_producto": "RETRO-009",
        "nombre": "Cámara Réflex Canon AE-1",
        "categoria": "Fotografía",
        "anio_fabricacion": 1976,
        "estado_conservacion": "Excelente (VG+)",
        "precio": 180.00,
        "stock": 1,
        "descripcion": "Cuerpo e incluye lente de 50mm f/1.8. Fotómetro funcionando con pila nueva.",
        "imagen_url": "https://images.unsplash.com/photo-1495707902641-75cac588d2e9?w=400"
    },
    {
        "id_producto": "RETRO-010",
        "nombre": "Disquete de instalación Windows 95",
        "categoria": "Computación",
        "anio_fabricacion": 1995,
        "estado_conservacion": "Detalles estéticos",
        "precio": 15.00,
        "stock": 5,
        "descripcion": "Set de disquetes de 3.5 pulgadas originales para nostálgicos del software.",
        "imagen_url": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"
    },
    {
        "id_producto": "RETRO-011",
        "nombre": "Reloj Casio F-91W Original",
        "categoria": "Accesorios",
        "anio_fabricacion": 1989,
        "estado_conservacion": "Como nuevo (Mint)",
        "precio": 25.00,
        "stock": 4,
        "descripcion": "El clásico reloj digital indestructible. Edición japonesa original.",
        "imagen_url": "https://images.unsplash.com/photo-1522312346375-d1a52e2b99b3?w=400"
    },
    {
        "id_producto": "RETRO-012",
        "nombre": "Tamagotchi Original Bandai",
        "categoria": "Juguetes",
        "anio_fabricacion": 1996,
        "estado_conservacion": "Buen estado",
        "precio": 50.00,
        "stock": 1,
        "descripcion": "Color carcasa azul translúcido. Con pila nueva incluida, listo para criar.",
        "imagen_url": "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?w=400"
    },
    {
        "id_producto": "RETRO-013",
        "nombre": "Sega Dreamcast",
        "categoria": "Consolas",
        "anio_fabricacion": 1999,
        "estado_conservacion": "Excelente (VG+)",
        "precio": 160.00,
        "stock": 1,
        "descripcion": "Lee copias y originales. Incluyen Visual Memory Unit (VMU) y cables.",
        "imagen_url": "https://images.unsplash.com/photo-1612036782180-6f0b6cd846fe?w=400"
    },
    {
        "id_producto": "RETRO-014",
        "nombre": "Televisor de Tubo (CRT) Sony Trinitron",
        "categoria": "Tecnología",
        "anio_fabricacion": 1992,
        "estado_conservacion": "Buen estado",
        "precio": 110.00,
        "stock": 1,
        "descripcion": "Pantalla de 14 pulgadas. Ideal para conectar consolas retro sin lag y con scanlines.",
        "imagen_url": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400"
    },
    {
        "id_producto": "RETRO-015",
        "nombre": "Casete Iron Maiden - The Number of the Beast",
        "categoria": "Música",
        "anio_fabricacion": 1982,
        "estado_conservacion": "Detalles estéticos",
        "precio": 20.00,
        "stock": 1,
        "descripcion": "Cinta en perfecto estado de reproducción. Carátula con leve desgaste por los años.",
        "imagen_url": "https://images.unsplash.com/photo-1611002214175-92576b92a2a1?w=400"
    }
]

@app.route('/')
def home():
    # Ahora le enviamos la LISTA COMPLETA de productos al HTML
    return render_template('producto.html', productos=lista_productos)

if __name__ == '__main__':
    app.run(debug=True)