# FastAPI ML Microservice 

#Микросервис на FastAPI, развёрнутый в Docker, который использует обученную модель машинного обучения (Random Forest на
#Iris dataset) для предсказания класса цветка по параметрам.

# Стек технологий

- Python 3.13
- FastAPI
- scikit-learn
- joblib
- Docker

#Как запустить локально

#1. Установить зависимости и обучи модель

pip install -r requirements.txt
python train_model.py

#2. Запусти FastAPI сервер

uvicorn main:app --reload

#3. Swagger UI:

#Перейти в браузере: [http://localhost:8000/docs](http://localhost:8000/docs)

#Docker

docker build -t fastapi-ml-service .
docker run -p 8000:8000 fastapi-ml-service

#Пример запроса

curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'

#Пример ответа:

{
  "prediction": "setosa"
}