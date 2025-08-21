 Evidencia GA7-220501096-AA5-EV01

 Descripción
Este proyecto implementa un servicio web con Flask que permite:
- Registrar usuarios.
- Iniciar sesión con verificación de credenciales.

Cumple con la evidencia solicitada en el componente Construcción de API.

---

Estructura del proyecto
```
NOMBRE_APELLIDO_AA5_EV01/
│── app.py              # Código principal
│── requirements.txt    # Dependencias
│── README.md           # Documentación
│── .gitignore          # Archivos ignorados
│
├── tests/              # Carpeta de pruebas
│    └── test_app.py
│
└── docs/               # Documentación adicional
     └── instrucciones.md
```

---

 Instalación y ejecución
1. Clonar el repositorio:
   ```bash
   git clone <URL_REPOSITORIO>
   cd NOMBRE_APELLIDO_AA5_EV01
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar la aplicación:
   ```bash
   python app.py
   ```

---

 Endpoints

 Registro
```
POST /registro
{
  "usuario": "juan",
  "password": "1234"
}
```

 Login
```
POST /login
{
  "usuario": "juan",
  "password": "1234"
}
```

---

  Pruebas automáticas
Ejecutar pruebas con:
```bash
pytest
```
