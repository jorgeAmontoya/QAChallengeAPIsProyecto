Feature: crear projectos
#@test_update_project
Scenario: editar proyecto exitosamente
Given que el usuario desea editar un proyecto
When edita el campo Internal donor name
Then se actualiza correctamente el projecto


#@test_update_project_without_id
Scenario: Intentar editar un proyecto sin enviar el ID
  Given que el usuario desea actualizar un proyecto existente
  When modifica el campo "Internal donor name" sin incluir el ID del proyecto en la solicitud
  Then el sistema debe rechazar la operación
  And mostrar un mensaje indicando que el ID del proyecto es obligatorio

#@test_update_project_without_token
Scenario: Intentar actualizar un proyecto sin enviar el token en los headers
  Given que el usuario cuenta con la información válida para editar un  proyecto
  When intenta editar  el proyecto sin enviar el token de autenticación en los headers
  Then el sistema debe rechazar la actualizacion del proyecto
  And mostrar un mensaje indicando que la autenticación es requerida status 401
