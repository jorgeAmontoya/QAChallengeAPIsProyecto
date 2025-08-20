Pruebas Playwright
######## Crud de projectos 
Prueba automatizada con Playwright en Python para validar crud de projectos hacia la página del COMMHEALTH

📌 Requisitos
Python 3.10 o superior
pip (administrador de paquetes de Python)
📦 Instalación de dependencias
Ejecuta el siguiente comando en la terminal para instalar Playwright y Pytest:

pip install playwright pytest
Después, instala los navegadores necesarios para Playwright:

playwright install
Esto descargará y configurará los navegadores compatibles (Chromium, Firefox y WebKit).

🚀 Cómo ejecutar las pruebas
Si quieres correr la prueba, usa:

pytest .\tests\api\test_create_project -s
pytest .\tests\api\test_create_existing_project -s
pytest .\tests\api\test_create_project_with_two_character_name -s
pytest .\tests\api\test_create_project_without_token -s


######## CONSULTAR API DE ProjectServices
Este proyecto contiene pruebas automatizadas de API utilizando Playwright con Python. Se realizan operaciones de tipo CRUD (Crear, Leer, Actualizar) sobre los servicios de la API ProjectServices.

Requisitos Previos
Antes de ejecutar las pruebas, asegúrate de tener instalado lo siguiente:

Python 3.10 o superior
Playwright para Python
Pytest para la ejecución de pruebas
Para instalar las dependencias necesarias (en caso no las hayas instalado en el ejemplo anterior), ejecuta:

pip install playwright pytest
playwright install
Estructura del Proyecto
test: Contiene las pruebas para la API.
pytest.ini: Archivo de configuración para pytest.
Ejecución de Pruebas
Para ejecutar las pruebas de la test/API, accede a la caperta API usa el siguiente comando:

pytest .\tests\api\test_create_project -s

Jorge Anderson Montoya
