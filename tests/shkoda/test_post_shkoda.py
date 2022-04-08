import pytest
from random import choice
from checker.general import Checker
from helpers.shkoda_helps import ShkodaHelps

def test_positive(base_fixture):
    car = ['KODIAQ', "KAROQ", "RAPID", "FELICIA"]

    dealer ="843"
    car = choice(car)
    first_name = 'Oleg'
    patronymic = 'Romanovich'
    last_name = 'Bashkirov'
    date =  "16.11.2020"
    time = "10:30"
    phone = base_fixture.helper.generate_phone()
    email = "test@test.ru"
    car_number =  base_fixture.helper.generate_car_number()
    vin = base_fixture.helper.generate_vin_code()

    response = base_fixture.api.shkoda.post_shkoda(dealer, car, first_name, patronymic, last_name, date, time, phone, email, car_number, vin)
    print(response.json())

    assert response.status_code == 201, 'Статус код не равен 201'
    assert response.json()['status'] == 'OK', 'Запись не прошла'

    check_resp = base_fixture.checker.validate_json(response.json(), 'schemas/shkoda_post.json')
    assert check_resp is True, 'тело запроса не соответствует схеме'

@pytest.mark.parametrize('date', ["05.11.2020", "08.11.2020", "09.11.2020"])
def test_positive_when_free_data(base_fixture, date):
    dealer ="843"
    car = 'KODIAQ'
    first_name = 'Oleg'
    patronymic = 'Romanovich'
    last_name = 'Bashkirov'
    phone = base_fixture.helper.generate_phone()
    time = '10:30'
    email = "test@test.ru"
    car_number =  base_fixture.helper.generate_car_number()
    vin = base_fixture.helper.generate_vin_code()

    response = base_fixture.api.shkoda.post_shkoda(dealer, car, first_name, patronymic, last_name, date, time, phone, email, car_number, vin)
    print(response.json())

    assert response.status_code == 201, 'Статус код не равен 201'
    assert response.json()['message'] == 'create_success', 'Запись к дилеру не удалась'
