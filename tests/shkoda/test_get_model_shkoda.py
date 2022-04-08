import pytest
import webbrowser
from checker.general import Checker


@pytest.mark.parametrize('model', ["KODIAQ", "KAROQ", "RAPID", "FELICIA", "ROOMSTER", "YETI"])
def test_positive_get_model_shkoda(base_fixture, model):
    response = base_fixture.api.shkoda.get_model_shkoda(model)
    print(response.json())

    webbrowser.open(response.json()['pic'])

    check_resp = base_fixture.checker.validate_json(response.json(), 'schemas/shkoda_get_model.json')
    assert check_resp is True, 'тело запроса не соответствует схеме'