# 🛒 Mercado Proyecto

Proyecto desarrollado en **Django** como parte de la práctica de creación y despliegue de aplicaciones web.  
Actualmente se encuentra funcionando en Render y el código fuente está disponible en GitHub.  

---

## 🚀 Ejecución en local

Sigue estos pasos para correr el proyecto en tu computadora:

### 1. Clonar el repositorio  
```bash
git clone https://github.com/RoloPython/mercado-proyecto.git
cd mercado-proyecto/mercado
```

### 2. Crear y activar el entorno virtual  
En **Windows (PowerShell):**
```bash
python -m venv venv
.env\Scriptsctivate
```

En **Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias  
```bash
pip install -r requirements.txt
```

### 4. Migrar la base de datos  
```bash
python manage.py migrate
```

### 5. Crear un superusuario (opcional)  
```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor  
```bash
python manage.py runserver
```

Accede al proyecto desde tu navegador en:  
👉 http://127.0.0.1:8000  

---

## 🌐 Versión en línea

El proyecto está desplegado en **Render**:  
👉 [https://mercado-proyecto.onrender.com](https://mercado-proyecto.onrender.com)

---

## 📂 Estructura del proyecto

```
mercado-proyecto/
│── mercado/              # Configuración principal del proyecto
│── tienda/               # Aplicación para productos / catálogo
│── accounts/             # Aplicación para autenticación de usuarios
│── templates/            # Archivos HTML
│── static/               # Archivos estáticos (CSS, JS)
│── db.sqlite3            # Base de datos SQLite
│── manage.py             # Script principal de Django
│── requirements.txt      # Dependencias del proyecto
```

---

## ⚙️ Tecnologías utilizadas

- Python 3.13  
- Django  
- SQLite  
- Gunicorn (para despliegue en Render)  

---

## 👨‍🏫 Autor

- **David Velázquez Zorrilla**  
Proyecto académico para práctica de desarrollo web con Django.  
