class Test_get_initiative:
    def test_api_get_initiative(self,get_token,playwright):
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
        assert response.status == 200
        json_data = response.json()

        first_project = json_data[0]
        request.dispose()