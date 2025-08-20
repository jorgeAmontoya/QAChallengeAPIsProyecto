from conftest import get_token


def test_api_get_project(create_project,get_token,playwright):
    name_project = "project para actualizar 17"
    token = "Bearer "+ get_token
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept":"text/plain",
            "Authorization":token
        }
    )
    response =create_project(name_project)
    print("*****esta es la id project OK****")
    print(response)
    body = response.json()
    idProject = body["id"]
    response = request.get(f"https://projectservicesqa.azurewebsites.net/api/Project/{idProject}")
    assert response.status == 200
    json_data = response.json()
    print(json_data)
    assert json_data["projectName"] == name_project
    request.dispose()
    print("Test completed successfuly")
