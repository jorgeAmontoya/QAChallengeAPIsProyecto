def test_get_project_without_token(playwright):
    token = "Bearer "
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept":"text/plain",
            "Authorization":token
        }
    )

    idProject = "122"
    response = request.get(f"https://projectservicesqa.azurewebsites.net/api/Project/{idProject}")
    assert response.status == 401
    json_data = response.json()
    print(json_data)
    print("Test completed successfuly")