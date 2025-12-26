REST API + ML скрипты для распознавания номеров контейнеров и прогнозирования временного ряда.

Скрипты: ocr_task/ocr.py → распознавание номеров  
 Скрипты: prediction_task/prediction.py → прогноз ряда  
 Эндпоинт: endpoint_task/endpoint.py → возвращает JSON с OCR и прогнозом

## Функционал

- OCR: распознаёт номера контейнеров на изображениях
- Прогноз: строит синтетический временной ряд, прогноз на 5 точек
- Эндпоинт `/predict`

# Установить зависимости

pip install -r requirements.txt

# Запуск OCR

python ocr_task/ocr.py

# Запуск прогноза

python prediction_task/prediction.py

# Запуск эндпоинта

uvicorn endpoint_task/endpoint:app --reload
API будет доступен на: http://127.0.0.1:8000/predict
