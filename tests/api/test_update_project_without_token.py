def test_update_project_without_token(playwright,create_project):
    name_project = "project para actualizar 12"
    projectDonorName = "projectDonorname update 1"
    response =create_project(name_project)
    print("*****esta es la id project OK****")
    print(response)
    body = response.json()
    idProject = body["id"]
    print("id de projecto es ****")
    print(idProject)
    payload = {
        "id": idProject,
        "projectName": "nombre actualizado3",
        "description": "Proyecto de prueba",
        "funderId": "eeeee",
        "stateId": 1,
        "priorityId": 1,
        "projectDonorName": "12345",
        "contractNumber": "ADFGGHH",
        "plannedStartDate": "2025-08-18T22:10:36.448Z",
        "plannedEndDate": "2025-08-19T05:00:00.000Z",
        "director": 1,
        "initiativeId": "122",
        "report": ["Daily"],
        "totalBudget": 100000,
        "inactive": False,
        "isDeleted": False
        }
    token = "Bearer "
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept": "application/json",
            "Authorization": token
        }
    )
    response = request.put(
        "https://projectservicesqa.azurewebsites.net/api/Project",
        data=payload
    )
    json_data = response.json()
    print("Respuesta update:", json_data)
    request.dispose()
    assert response.status == 401