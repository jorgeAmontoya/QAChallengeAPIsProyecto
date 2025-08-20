def test_update_project(create_project,update_project):
    projectDonorName = "projectDonorname update 1"
    idProject = None
    print("id de projecto es ****")
    print(idProject)
    responseUpdate = update_project(idProject,projectDonorName)
    print("*****esta es la respuesta****")
    print(responseUpdate)
    assert responseUpdate.status == 400