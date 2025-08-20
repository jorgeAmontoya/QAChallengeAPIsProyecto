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

Bugs encontrados durante las pruebas:

🐞 Bug 1

ID: BUG-001
Título: El sistema permite crear proyectos con nombres de menos de 3 caracteres.

Severidad: Alta
Prioridad: Alta
Ambiente: http://128.85.27.33:3000/planner/projects

Precondición: El usuario cuenta con token de autenticación válido.

Pasos para reproducir:

Enviar una petición POST al endpoint https://projectservicesqa.azurewebsites.net/api/Project

Incluir en el body un nombre de proyecto con 2 caracteres (ejemplo: "AB").

Completar los demás campos requeridos con valores válidos.

Ejecutar la solicitud.

Datos de prueba:

{
    "projectName": "ta",
    "description": "descrptionb text",
    "funderId": 121,
    "stateId": 1,
    "priorityId": 1,
    "projectDonorName": "jorge",
    "contractNumber": "ADFGGHH",
    "plannedStartDate": "2025-08-18T22:10:36.448Z",
    "plannedEndDate": "2025-08-19T05:00:00.000Z",
    "director": 1,
    "initiativeId": 9,
    "report": [
        "Daily"
    ],
    "totalBudget": 100000
}


Resultado obtenido:
✔️ El sistema permite crear el proyecto con un nombre de 2 caracteres.

Resultado esperado:
❌ El sistema no debe permitir la creación del proyecto.
❌ Debe retornar un mensaje de validación indicando que el nombre debe tener mínimo 3 caracteres.
❌ El status code esperado es 400 (Bad Request).

Notas adicionales:
Este bug puede generar inconsistencias en los datos, ya que se violan las reglas de negocio definidas para la longitud mínima del nombre del proyecto.

🐞 Bug 2

ID: BUG-002
Título: El sistema no retorna status code 409 al crear un proyecto con nombre existente.

Severidad: Media
Prioridad: Alta
Ambiente: http://128.85.27.33:3000/planner/projects

Precondición: Existe un proyecto previamente creado con el nombre "QATest".

Pasos para reproducir:

Enviar una petición POST al endpoint https://projectservicesqa.azurewebsites.net/api/Project

Incluir en el body un nombre de proyecto ya existente (ejemplo: "QATest").

Completar los demás campos requeridos con valores válidos.

Ejecutar la solicitud.

Datos de prueba:

{
    "projectName": "QATest",
    "description": "descrptionb text",
    "funderId": 121,
    "stateId": 1,
    "priorityId": 1,
    "projectDonorName": "jorge",
    "contractNumber": "ADFGGHH",
    "plannedStartDate": "2025-08-18T22:10:36.448Z",
    "plannedEndDate": "2025-08-19T05:00:00.000Z",
    "director": 1,
    "initiativeId": 9,
    "report": [
        "Daily"
    ],
    "totalBudget": 100000
}


Resultado obtenido:
✔️ El sistema retorna status code 400 (Bad Request).

Resultado esperado:
❌ El sistema debe retornar status code 409 (Conflict), indicando que ya existe un proyecto con el mismo nombre.

Notas adicionales:
El uso de un status code incorrecto puede afectar la interpretación de errores por parte de aplicaciones clientes, dificultando la implementación de controles adecuados.


