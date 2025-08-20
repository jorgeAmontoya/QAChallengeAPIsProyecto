Feature: crear projectos
#@test_create_project
Scenario: Crear proyecto exitosamente
Given que el usuario desea crear un nuevo proyecto
When obtiene la informacion necesaria para la creacion
Then se crea correctamente el projecto

#@test_create_existing_project
Scenario: Intentar crear un proyecto con un nombre ya existente
  Given que el usuario quiere crear un nuevo proyecto
  When intenta registrar el proyecto con un nombre que ya existe
  Then el sistema no debe permitir la creación del proyecto
  And debe mostrar un mensaje indicando que el nombre ya está en uso con status 409

#@test_create_project_with_two_character_name
Scenario: Intentar crear un proyecto con dos caracteres
  Given que el usuario quiere crear un nuevo proyecto
  When intenta registrar el proyecto con un nombre con 2 caracteres
  Then el sistema no debe permitir la creación del proyecto
  And debe mostrar un mensaje indicando que el nombre debe ser minimo de 3 caracteres


#@test_create_project_without_token
Scenario: Intentar crear un proyecto válido sin enviar el token en los headers
  Given que el usuario cuenta con la información válida para crear un nuevo proyecto
  When intenta registrar el proyecto sin enviar el token de autenticación en los headers
  Then el sistema debe rechazar la creación del proyecto
  And mostrar un mensaje indicando que la autenticación es requerida status 401

