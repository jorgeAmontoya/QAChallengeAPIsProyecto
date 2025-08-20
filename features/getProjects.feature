Feature: Obtener projectos
#@test_get_project_by_id
Scenario: Obtener un proyecto existente por su ID  
  Given que el usuario desea consultar la información de un proyecto  
  When solicita el proyecto proporcionando su ID  
  Then el sistema devuelve la información correspondiente al proyecto 

#@test_get_project_with_id_not_existing
Scenario: Consultar un proyecto con un ID inexistente  
  Given que el usuario desea consultar la información de un proyecto  
  When solicita el proyecto proporcionando un ID que no existe  
  Then el sistema no devuelve información y muestra un mensaje indicando que el proyecto no fue encontrado

@test_get_project_without_token
Scenario: Consultar un proyecto sin enviar el token de autenticación  
  Given que el usuario desea obtener la información de un proyecto  
  When realiza la solicitud sin incluir el token de autenticación en los headers  
  Then el sistema rechaza la petición  
  And muestra un mensaje indicando que la autenticación es requerida con el estado 401 
