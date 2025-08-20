def test_get_token(playwright):
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept":"application/json",
            "Authorization":"Basic Y2FuZGlkYXRvX3FhXzAxQGdtYWlsLmNvbTpQcnVlYmExIQ=="
        }
    )
    response = request.post("https://securityservicesqa.azurewebsites.net/api/Authenticate/token")
    json_data = response.json()
   # print(json_data)
    assert response.status == 200
    token = json_data["token"]
    print("este es el token" + token)
    #assert json_data["id"] ==1

    request.dispose()
    print("Test completed successfuly")

    