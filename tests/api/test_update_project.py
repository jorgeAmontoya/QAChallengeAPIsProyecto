from conftest import update_project


def test_update_project(create_project,update_project):
    name_project = "project para actualizar 7"
    projectDonorName = "projectDonorname update 1"

    response =create_project(name_project)

    print("*****esta es la id project OK****")
    print(response)
    body = response.json()
    idProject = body["id"]


    print("id de projecto es ****")
    print(idProject)

    responseUpdate = update_project(idProject,projectDonorName)


    print("*****esta es la respuesta****")
    print(responseUpdate)
    assert responseUpdate.status == 200