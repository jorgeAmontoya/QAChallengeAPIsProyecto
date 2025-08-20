from conftest import create_project


def test_create_existing_project(create_project):
    name_project = "projectRepeatedjoruuu2"
    
    response =create_project(name_project)

    print("*****esta es la respuesta OK****")
    print(response)

    response2 = create_project(name_project)


    print("*****esta es la respuesta****")
    print(response2)
    assert response2.status == 409
