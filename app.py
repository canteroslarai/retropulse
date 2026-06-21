from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Registro principal de productos
# Clave primaria: ID_PRODUCTO

productos = [
    {
        "id": 1,
        "nombre": "Consola Sega Mega Drive",
        "categoria": "Videojuegos Retro",
        "precio": 85000,
        "stock": 4,
        "descripcion": "Consola clásica de los años 90"
    },

    {
        "id": 2,
        "nombre": "Cámara Polaroid Vintage",
        "categoria": "Coleccionables",
        "precio": 60000,
        "stock": 3,
        "descripcion": "Cámara instantánea antigua restaurada"
    },

    {
        "id": 3,
        "nombre": "Walkman Sony Original",
        "categoria": "Tecnología Retro",
        "precio": 45000,
        "stock": 6,
        "descripcion": "Reproductor portátil clásico"
    }
]


# Página principal
@app.route("/")
def inicio():
    return render_template("index.html", productos=productos)


# Registrar producto nuevo
@app.route("/registrar", methods=["POST"])
def registrar():

    nuevo_producto = {

        "id": len(productos) + 1,

        "nombre": request.form["nombre"],

        "categoria": request.form["categoria"],

        "precio": request.form["precio"],

        "stock": request.form["stock"],

        "descripcion": request.form["descripcion"]
    }


    productos.append(nuevo_producto)


    return redirect("/")



# Eliminar producto
@app.route("/eliminar/<int:id>")
def eliminar(id):

    for producto in productos:

        if producto["id"] == id:

            productos.remove(producto)

            break


    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)