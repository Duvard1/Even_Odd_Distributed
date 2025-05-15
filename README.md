# 📦 Even_Odd_Distributed
Even_Odd_Distributed es una aplicación de arquitectura distribuida basada en microservicios, desarrollada con Flask y Docker. Permite al usuario ingresar un número y determinar si es par o impar a través de la comunicación entre dos servicios (app-a y app-b).

# 🚀 Tecnologías usadas
- Python 3.10
- Flask
- Docker
- Docker Compose
- HTML + CSS
- Arquitectura distribuida con microservicios

# 🧠 Estructura del Proyecto
![image](https://github.com/user-attachments/assets/3aad492c-7b61-48fd-83f3-def18f304045)

# ⚙️ Cómo funciona
- app-a: es un servicio Flask que muestra un formulario HTML. El usuario ingresa un número.
- app-b: es otro servicio Flask que recibe un número por URL y responde si es "Par" o "Impar".
- Ambos servicios se comunican por HTTP internamente a través de la red de Docker.

# 🐳 Cómo desplegarlo con Docker
1. Clona el repositorio: 
``
git clone https://github.com/tu-usuario/Even_Odd_Distributed.git
``
2. Construye las imágenes: 
``
docker-compose build
`` 
3. Inicia los servicios:
``
docker-compose up
`` 

# 🌐 Acceso a la app
Abre tu navegador y visita:
👉 http://localhost:5000






