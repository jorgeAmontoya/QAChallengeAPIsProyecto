from behave import given, then, when
from conftest import get_initiative, get_token
from tests.api.test_get_initiative import Test_get_initiative
from utils.apiGetFounder import apiGetFounder
from utils.getInitiative import test_api_get_initiative

idInitiative = ""
idFunder = ""
response = ""
project_data=""

@given('que el usuario desea crear un nuevo proyecto')
def step_given(context):
    test_api_get_initiative = Test_get_initiative()
    idInitiative = test_api_get_initiative.test_api_get_initiative()
    print(idInitiative)
    project_data = {
    "projectName": "testjorge2",
    "description": "descrptionb text",
    "funderId": idFunder,
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

@when('obtiene la informacion necesaria para la creacion')
def step_when(context,playwright):
    
    token = "Bearer "+ get_token()
    with sync_playwright() as p:
        request = p.request.new_context( 
        extra_http_headers={
            "Accept":"application/json",
            "Authorization":token
        }
    )
    response = request.post("https://projectservicesqa.azurewebsites.net/api/Project",
                 json_data = project_data          )
    json_data = response.json()

    first_project = json_data[0]
    request.dispose()
    
    
@then('se crea correctamente el projecto')
def step_then(context):
    assert response.status == 200
