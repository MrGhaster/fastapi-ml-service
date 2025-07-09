# FastAPI ML Microservice

# Микросервис на FastAPI, развёрнутый в Docker, который использует обученную модель машинного обучения (Random Forest на
# Iris dataset) для предсказания класса цветка по параметрам.

# Стек технологий

- Python 3.13
- FastAPI
- scikit-learn
- joblib
- Docker
- Pandas

# Как запустить локально

# 1. Создать и активировать виртуальное окружение:

python -m venv venv
.\venv\Scripts\Activate.ps1  # Для PowerShell в Windows
# или
# source venv/bin/activate  # Для Linux/macOS

# 2. Установить зависимости и обучить модель:

pip install -r requirements.txt
python train_model.py

# 3. Запустить FastAPI

uvicorn main:app --reload  # Или uvicorn main:app для production

# 4. Docker:

docker build -t fastapi-ml-service .
docker run -d -p 8000:80 fastapi-ml-service

# 5. Swagger UI:

# Перейти в браузере: [http://localhost:8000/docs](http://localhost:8000/docs)

# Пример запроса

curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'

# Пример ответа:

{
  "prediction": "setosa"
}