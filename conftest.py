import pytest
import requests
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture
def get_token(playwright):
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept": "application/json",
            "Authorization": "Basic Y2FuZGlkYXRvX3FhXzAxQGdtYWlsLmNvbTpQcnVlYmExIQ=="
        }
    )
    response = request.post("https://securityservicesqa.azurewebsites.net/api/Authenticate/token")
    json_data = response.json()
    assert response.status == 200
    token = json_data["token"]
    request.dispose()
    return token

@pytest.fixture
def get_initiative(get_token,playwright):
        body = {
        "rows": 50,
        "page": 1,
        "sort": [
            {
                "field": "name",
                "dir": "asc"
            }
        ],
        "filter": [
            {
                "field": "isDeleted",
                "value": "false",
                "matchMode": "equals"
            }
        ]
    }

        token = "Bearer "+ get_token
        request = playwright.request.new_context(
            extra_http_headers={
                "Accept":"application/json",
                "Authorization":token
            }
        )
        response = request.post("https://projectservicesqa.azurewebsites.net/api/Initiative/GetInitiative",
                    data = body          )
        json_data = response.json()
        first_initiative = json_data[0]
        request.dispose()
        print("************initiativa desde conftest")
        print(first_initiative)
        return first_initiative

@pytest.fixture
def get_founder(get_token,playwright):
    body = {"rows":100,"page":1,"sort":[{"field":"name","dir":"asc"}],"filter":[{"field":"isDeleted","value":"false","matchMode":"equals"}]}

    token = "Bearer "+ get_token
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept":"application/json",
            "Authorization":token
        }
    )
    response = request.post(
         "https://projectservicesqa.azurewebsites.net/api/ProjectFunder/GetProjectsFunders",
          data = body         
        )
    json_data = response.json()

    first_Founder = json_data[0]
    request.dispose()
    print("************founder desde conftest")
    print(first_Founder)
    return first_Founder

@pytest.fixture
def create_project(get_token, playwright, get_initiative, get_founder):
    def _create_project(name_project: str):
        payload = {
            "projectName": name_project,
            "description": "Proyecto de prueba",
            "funderId": get_founder["id"],
            "stateId": 1,
            "priorityId": 1,
            "projectDonorName": "jorge",
            "contractNumber": "ADFGGHH",
            "plannedStartDate": "2025-08-18T22:10:36.448Z",
            "plannedEndDate": "2025-08-19T05:00:00.000Z",
            "director": 1,
            "initiativeId": get_initiative["id"],
            "report": ["Daily"],
            "totalBudget": 100000
        }
        token = f"Bearer {get_token}"
        request = playwright.request.new_context(
            extra_http_headers={
                "Accept": "application/json",
                "Authorization": token
            }
        )
        response = request.post(
            "https://projectservicesqa.azurewebsites.net/api/Project",
            data=payload
        )
        json_data = response.json()
        print("Respuesta creación:", json_data)
        return response
    return _create_project

@pytest.fixture
def update_project(get_token, playwright, get_initiative, get_founder):
    def _update_project(id_project: str,projectDonorName:str):
        payload = {
            "id": id_project,
            "projectName": "nombre actualizado3",
            "description": "Proyecto de prueba",
            "funderId": get_founder["id"],
            "stateId": 1,
            "priorityId": 1,
            "projectDonorName": projectDonorName,
            "contractNumber": "ADFGGHH",
            "plannedStartDate": "2025-08-18T22:10:36.448Z",
            "plannedEndDate": "2025-08-19T05:00:00.000Z",
            "director": 1,
            "initiativeId": get_initiative["id"],
            "report": ["Daily"],
            "totalBudget": 100000,
            "inactive": False,
            "isDeleted": False
        }
        token = f"Bearer {get_token}"
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
        print("Respuesta creación:", json_data)
        request.dispose()
        return response
    return _update_project
