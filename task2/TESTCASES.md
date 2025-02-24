# [Задание 2.1](https://github.com/avito-tech/tech-internship/blob/main/Tech%20Internships/QA/QA-trainee-assignment-winter-2025/QA-trainee-assignment-winter-2025.md#%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-21)

## 1. Тест-кейсы ручки создания объявления

| Название | `create_item__test`                                               |
|:---------|:------------------------------------------------------------------|
| Шаги     | Отправить POST-запрос на /api/1/item с корректными данными.       |
| ОП       | Статус ответа: 200. В ответе содержится уникальный id объявления. |

Далее предполагаем, что поля `name` и `price` обязательные при создании объявления.

| Название | `create_item__item_has_name_test`                       |
|:---------|:--------------------------------------------------------|
| Шаги     | Отправить `POST`-запрос на /api/1/item без поля `name`. |
| ОП       | Статус ответа: 400.                                     |

| Название | `create_item__item_has_price_test`                     |
|:---------|:-------------------------------------------------------|
| Шаги     | Отправить POST-запрос на /api/1/item без поля `price`. |
| ОП       | Статус ответа: 400.                                    |

| Название | `create_item__item_invalid_price_test`                              |
|:---------|:--------------------------------------------------------------------|
| Шаги     | Отправить POST-запрос на /api/1/item c отрицательным полем `price`. |
| ОП       | Статус ответа: 400.                                                 |

## 2. Тест-кейсы ручки получения объявления по его `id`

| Название | `get_item_by_id__test`                                                          |
|:---------|:--------------------------------------------------------------------------------|
| Шаги     | Отправить GET-запрос на /api/1/item/{id} c `id` существующего объявления.       |
| ОП       | Статус ответа: 200. Поле `id` в ответе совпадает с `id` переданного объявления. |

| Название | `get_item_by_id__invalid_id_test`                                            |
|:---------|:-----------------------------------------------------------------------------|
| Шаги     | Отправить GET-запрос на /api/1/item/{id} c `id` НЕ существующего объявления. |
| ОП       | Статус ответа: 400.                                                          |

| Название | `get_item_by_id__correct_info_test`                                                                                                                |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| Шаги     | 1) Отправить POST-запрос на /api/1/item с корректными данными, в ответе получить `id` объявления.<br/>2) Отправить GET-запрос на /api/1/item/{id}. |
| ОП       | Статус ответа: 200. Полученные данные совпадают с переданными при создании.                                                                        |

## 3. Тест-кейсы ручки получения всех объявлений по `sellerID`

| Название | `get_items_by_sellerID__test`                                                       |
|:---------|:------------------------------------------------------------------------------------|
| Шаги     | Отправить GET-запрос на /api/1/{sellerID}/item c `sellerID` существующего продавца. |
| ОП       | Статус ответа: 200. Тело ответа содержит массив объявлений либо пустой массив.      |

| Название | `get_items_by_sellerID__invalid_sellerID_test`                                         |
|:---------|:---------------------------------------------------------------------------------------|
| Шаги     | Отправить GET-запрос на /api/1/{sellerID}/item c `sellerID` НЕ существующего продавца. |
| ОП       | Статус ответа: 400.                                                                    |

| Название | `get_items_by_sellerID__create_new_item_test`                                                                                                                                           |
|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Шаги     | 1) Отправить POST-запрос на /api/1/item с корректными данными, в ответе получить `id` объявления.<br/>2) Отправить GET-запрос на /api/1/{sellerID}/item c `sellerID` созданного айтема. |
| ОП       | Статус ответа: 200. Последний айтем в списке айтемов селлера - только что созданный айтем.                                                                                              |

## 4. Тест-кейсы ручки получения статистики по `id` айтема

| Название | `get_item_statistic_by_id__test`                                                |
|:---------|:--------------------------------------------------------------------------------|
| Шаги     | Отправить GET-запрос на /api/1/statistic/{id} c `id` существующего объявления.. |
| ОП       | Статус ответа: 200. Тело ответа содержит данные статистики.                     |

| Название | `get_item_statistic_by_id__invalid_id_test`                                        |
|:---------|:-----------------------------------------------------------------------------------|
| Шаги     | Отправить GET-запрос на /api/1/statistic/{id} c `id` НЕ существующего объявления.. |
| ОП       | Статус ответа: 400.                                                                |

| Название | `get_item_statistic_by_id__correct_info_test`                                                                                                                                    |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Шаги     | 1) Отправить POST-запрос на /api/1/item с корректными данными, в ответе получить `id` объявления.<br/>2) Отправить GET-запрос на /api/1/statistic/{id} c `id` созданного айтема. |
| ОП       | Статус ответа: 200. Статистика полученного айтема соответствует статистике созданного.                                                                                           |