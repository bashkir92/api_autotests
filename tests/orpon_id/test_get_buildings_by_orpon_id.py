import pytest
from checker.general import Checker

def test_positive(base_fixture):
    id = 72501163
    session_token = base_fixture.configs.token
    response = base_fixture.api.orpon_id.get_buildings_by_orpon_id(id, session_token)
    fact_resp = response.json()

    assert response.status_code == 200, "Статус код не равен 200"

    check_resp = base_fixture.checker.validate_json(response.json(), 'schemas/orpon_id.json')
    assert check_resp is True, 'тело запроса не соответствует схеме'

    assert fact_resp['data']["orpon_id"] == id, 'Орпон дома не соответствует испрашиваемому'

def test_negative(base_fixture):
    id = 'ghfgh'
    session_token = base_fixture.configs.token
    response = base_fixture.api.orpon_id.get_buildings_by_orpon_id(id, session_token)

    assert response.status_code == 400, "Статус код не равен 400"

