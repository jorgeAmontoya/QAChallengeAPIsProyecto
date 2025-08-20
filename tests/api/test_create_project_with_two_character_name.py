def test_create_project_with_two_character_name(create_project):
    name_project = "pr"
    response =create_project(name_project)
    print("*****esta es la respuesta fail por caracteres menores a 3")
    print(response)
    assert response.status == 400