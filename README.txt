Проект автоматизации тестирования REST API

clients- папка для хранения клиентов апи, БД, и т.д.
helpers - папка для хранения хелперов
schemas - папка с json схемами используемыми в тестируемом АПИ сервисе
checkers - папка для хранения методов проверки ответов запросов
tests - папка с тестами
application.py - файл, содержащий объекты клиентов, конфигурации и т.д.
config.py - файл с настройками конфигурации
conftest.py - файл с фикстурами


В проекте демонстрируется автоматизация ручек
https: ... #/common/get_api_v4_flatgramms_buildings_orpon_id__orpon_id_                  GET
https: ... #/common/get_api_v4_flatgramms_buildings_buildings_id                         GET
https: ... #/common/get_api_v4_devices_codes                                             DELETE


https://app.swaggerhub.com/apis/artem.plut/service/1.0.0#/default/makeServiceRequest     POST
https://app.swaggerhub.com/apis/artem.plut/service/1.0.0#/default/getModel               GET
https://app.swaggerhub.com/apis/artem.plut/service/1.0.0#/default/getCities              GET
https://app.swaggerhub.com/apis/artem.plut/service/1.0.0#/default/getCars                GET
https://app.swaggerhub.com/apis/artem.plut/service/1.0.0#/default/getDealers             GET
