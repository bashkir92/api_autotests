def test_get_cars(base_fixture):
    response = base_fixture.api.shkoda.get_cars()
    print(response.json()[3])

    assert response.status_code == 200, 'Статус код не равен 200'