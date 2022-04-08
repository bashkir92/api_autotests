from checker.general import Checker

def test_get_city(base_fixture):
    response = base_fixture.api.shkoda.get_city()
    print(response.json())

    check_resp = base_fixture.checker.validate_items(response.json(), 'schemas/shkoda_get_city.json')
    assert check_resp == {True}, 'тело запроса не соответствует схеме'