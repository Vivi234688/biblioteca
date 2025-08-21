"""
API de ejemplo para registro e inicio de sesión
Cumple con la evidencia GA7-220501096-AA5-EV01
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulación de base de datos en memoria
usuarios = {}

@app.route('/registro', methods=['POST'])
def registrar():
    """
    Endpoint para registrar un nuevo usuario.
    Requiere: usuario, password
    """
    data = request.json
    usuario = data.get("usuario")
    password = data.get("password")

    if usuario in usuarios:
        return jsonify({"mensaje": "El usuario ya existe"}), 400

    usuarios[usuario] = password
    return jsonify({"mensaje": f"Usuario {usuario} registrado exitosamente"}), 201


@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint para iniciar sesión.
    Verifica si el usuario y contraseña son correctos.
    """
    data = request.json
    usuario = data.get("usuario")
    password = data.get("password")

    if usuarios.get(usuario) == password:
        return jsonify({"mensaje": "Autenticación satisfactoria"}), 200
    else:
        return jsonify({"mensaje": "Error en la autenticación"}), 401


if __name__ == '__main__':
    app.run(debug=True)
