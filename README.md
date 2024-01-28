# Тестовое задание

## Запуск

Для запуска приложения были написаны Dockerfile и docker-compose 

Запуск происходит командой
docker compose up --build Приложение будет доступно на localhost:8000

## База данных

Используется postgresql, поднятая с помощью docker image

## Описание
Реализованы 3 эндпоинта :
- add_product_to_recipe/
- cook_recipe/
- show_recipes_without_product/
### Согласно названиям каждой из функций задания. Для оптимизации кода я бы использовала кеширование с помощью redis и celery таски, но в угоду скорости разработки я лишь оптимизировала запросы в базу данных prefetch_related, где это требовалось.
Примеры работы
- add_product_to_recipe/
![Снимок экрана (1)](https://github.com/alantsupova/mirgovorit_test_task/assets/125733793/11e8f734-a903-47d8-a380-ccf59269f9c4)
![Снимок экрана (2)](https://github.com/alantsupova/mirgovorit_test_task/assets/125733793/d2f8e8ea-fbee-4e6c-a019-0dca5473632b)
![Снимок экрана (3)](https://github.com/alantsupova/mirgovorit_test_task/assets/125733793/7d5bb19f-1660-4c2d-84c0-409136cdfb5a)
- cook_recipe/
  ![Снимок экрана (4)](https://github.com/alantsupova/mirgovorit_test_task/assets/125733793/e4250b4e-ded4-4665-bb4c-84deaa631773)
![Снимок экрана (5)](https://github.com/alantsupova/mirgovorit_test_task/assets/125733793/22da7fba-39c9-49f2-b47b-9946fe514816)
![Снимок экрана (6)](https://github.com/alantsupova/mirgovorit_test_task/assets/125733793/d9a5d9e2-748a-42ca-a137-aa40e54f33d3)
- show_recipes_without_product/
![Снимок экрана (7)](https://github.com/alantsupova/mirgovorit_test_task/assets/125733793/65ab0e02-b037-491e-aba7-63c92c90a433)



Буду рада обратной связи :)
