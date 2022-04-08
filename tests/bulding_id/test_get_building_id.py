import pytest

@pytest.mark.parametrize('id', ["4156", "4722", "4064", "4068"])
def test_positive(base_fixture, id):
    session_token = base_fixture.configs.token
    response = base_fixture.api.building_id.get_buildings_by_building_id(id, session_token)
    print(response.json())

    assert response.status_code == 200, "Статус код не равен 200"


def test_negative(base_fixture):
    id = 'ghfgh'
    session_token = base_fixture.configs.token
    response = base_fixture.api.building_id.get_buildings_by_building_id(id, session_token)

    assert response.status_code == 400, "Статус код не равен 400"
