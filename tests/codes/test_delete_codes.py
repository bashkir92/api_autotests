def test_positive(base_fixture):
    id = 80477
    session_token = base_fixture.configs.token
    response = base_fixture.api.codes.delete_codes_by_id(id, session_token)
    print(response.status_code)

    assert response.status_code == 204, "Статус код не равен 204"


def test_negative(base_fixture):
    id = 'ghfgh'
    session_token = base_fixture.configs.token
    response = base_fixture.api.codes.delete_codes_by_id(id, session_token)

    assert response.status_code == 400, "Статус код не равен 400"