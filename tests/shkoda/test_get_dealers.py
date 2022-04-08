def test_get_dealers(base_fixture):
    response = base_fixture.api.shkoda.get_dealers()
    print(response.json())

    assert response.status_code == 200, 'Статус код не равен 200'
