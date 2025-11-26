// ...existing code...
# 🌱 AgroApp — API Agrícola

API backend desarrollada con Django y Django REST Framework para gestionar cultivos, cosechas, pérdidas agrícolas y generar reportes e indicadores.

---

## 📌 Resumen
AgroApp permite:
- CRUD de cultivos, cosechas y pérdidas.
- Cálculo de indicadores y reportes por temporada.
- Documentación automática (Swagger / Redoc).
- Estructura modular preparada para autenticación y despliegue.

---

## 📦 Tecnologías
- Python 3.12+
- Django 5.x
- Django REST Framework
- drf-yasg (Swagger / Redoc)
- SQLite (por defecto) / PostgreSQL (opcional)
- virtualenv / venv

---

## 📁 Estructura del proyecto (resumen)
agroapp/
├── cultivos/ (models, serializers, views, urls)  
├── cosechas/ (models, serializers, views, urls)  
├── perdidas/ (models, serializers, views, urls)  
├── reportes/ (views, urls)  
└── config/ (settings.py, urls.py)

---

## ⚙️ Instalación (Windows)
1. Clonar repositorio
```powershell
git clone https://github.com/tu_usuario/agroapp.git
cd agroapp
```
2. Crear y activar entorno virtual
```powershell
python -m venv v_agroapp
v_agroapp\Scripts\activate
```
3. Instalar dependencias
```powershell
pip install -r requirements.txt
```
4. Migrar base de datos
```powershell
python manage.py makemigrations
python manage.py migrate
```
5. Ejecutar servidor
```powershell
python manage.py runserver
```

(Para Linux/macOS usar `source v_agroapp/bin/activate`)

---

## 📊 Endpoints principales (prefijo: /api/)
- Cultivos — /api/cultivos/
  - GET /api/cultivos/ — listar
  - POST /api/cultivos/ — crear
  - GET /api/cultivos/{id}/ — detalle
  - PUT /api/cultivos/{id}/ — actualizar
  - DELETE /api/cultivos/{id}/ — eliminar

- Cosechas — /api/cosechas/
  - GET /api/cosechas/ — listar
  - POST /api/cosechas/ — crear
  - GET /api/cosechas/?lote=XYZ — filtrar por lote

- Pérdidas — /api/perdidas/
  - GET /api/perdidas/ — listar
  - POST /api/perdidas/ — crear
  - PUT /api/perdidas/{id}/ — actualizar
  - DELETE /api/perdidas/{id}/ — eliminar

- Reportes — /api/reportes/
  - GET /api/reportes/indicadores/?inicio=YYYY-MM-DD&fin=YYYY-MM-DD  
    Respuesta ejemplo: { "rendimiento_total": 1234.5, "porcentaje_promedio_perdida": 4.2, "rendimiento_neto_estimado": 1180.3 }
  - GET /api/reportes/temporada/?anio=2024&temporada=verano

Ejemplo curl:
```bash
curl "http://127.0.0.1:8000/api/reportes/indicadores/?inicio=2024-01-01&fin=2024-12-31"
```

---

## 📈 Definición de temporadas (configurable)
- primavera: septiembre — noviembre (9–11)  
- verano: diciembre — febrero (12–2)  
- otoño: marzo — mayo (3–5)  
- invierno: junio — agosto (6–8)

(Ajustar según región si es necesario.)

---

## 🔍 Documentación automática
- Swagger UI: /swagger/  
- Redoc: /redoc/  
- OpenAPI JSON: /swagger.json

---

## 🔒 Seguridad y configuración recomendada
- Variables sensibles en .env (SECRET_KEY, DATABASE_URL).
- Opcionales: Token Auth, JWT (simplejwt), CORS (django-cors-headers), permisos por rol.
- Configurar logging y settings por entornos (development/production).

---

## 🧪 Pruebas
- Usar Django TestCase y rest_framework.test.APIClient.
- Puedo generar una colección Postman (postman_collection.json) si la deseas.

---

## 🧾 Contribución
- Abrir issues para bugs o mejoras.
- Crear pull requests desde ramas con pruebas y descripción clara.

---

## 🧑‍💻 Autor y licencia
- Autor: Alicia — AgroApp Developer  
- Licencia: MIT

---

¿Deseas que genere alguno de estos archivos adicionales?
- Colección Postman (postman_collection.json)  
- requirements.txt completo  
- Diagrama UML básico  
- README en PDF  
- Banner/logo del repositorio
// ...existing code...