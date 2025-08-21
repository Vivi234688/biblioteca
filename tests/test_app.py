import json
from app import app

def test_registro_y_login():
    cliente = app.test_client()

    # Registro de usuario
    respuesta = cliente.post('/registro', json={"usuario": "juan", "password": "1234"})
    assert respuesta.status_code in [201, 400]  # Puede ser exitoso o ya existente

    # Login exitoso
    respuesta = cliente.post('/login', json={"usuario": "juan", "password": "1234"})
    assert respuesta.status_code == 200

    # Login fallido
    respuesta = cliente.post('/login', json={"usuario": "juan", "password": "malo"})
    assert respuesta.status_code == 401
