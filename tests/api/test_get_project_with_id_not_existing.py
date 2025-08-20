def test_get_project_with_id_not_existing(get_token,playwright):
    token = "Bearer "+ get_token
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept":"text/plain",
            "Authorization":token
        }
    )
    idProject = "0"
    response = request.get(f"https://projectservicesqa.azurewebsites.net/api/Project/{idProject}")
    assert response.status == 400
    request.dispose()
    print("Test completed successfuly")