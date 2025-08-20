def test_create_project_without_token(get_token,playwright,get_initiative,get_founder):
    idInitiative = get_initiative["id"]
    print("*********************esta es la iniciativa*****************")
    print(idInitiative)
    idFounder = get_founder["id"]
    project_data = {
        "projectName": "tjjejjjjjjjjjjjjhhh",
        "description": "descrptionb text",
        "funderId": idFounder,
        "stateId": 1,
        "priorityId": 1,
        "projectDonorName": "jorge",
        "contractNumber": "ADFGGHH",
        "plannedStartDate": "2025-08-18T22:10:36.448Z",
        "plannedEndDate": "2025-08-19T05:00:00.000Z",
        "director": 1,
        "initiativeId": idInitiative,
        "report": ["Daily"],
        "totalBudget": 100000
    }

    token = "Bearer "+ ""
    request = playwright.request.new_context( 
        extra_http_headers={
        "Accept":"application/json",
        "Authorization":token
        }
    )
    response = request.post(
        "https://projectservicesqa.azurewebsites.net/api/Project",
        data = project_data          
        )
    json_data = response.json()
    print(json_data)
  
    request.dispose()
    assert response.status == 401