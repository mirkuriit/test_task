


.env
```commandline
POSTGRES_DB=test_task
POSTGRES_USER=postgres
POSTGRES_PASSWORD=pg
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8000
FASTAPI_DB_HOST=localhost
```


Инструкция по запуску
```commandline
git clone git@github.com:mirkuriit/test_task.git
cd test_task

touch .env  ### пример .env выше
### Поднимаем только постгрес, соединить с бекендом не успел
docker compose up

poetry env use python3.13
poetry install

### Инициализация таблички 
poetry run init-db
### Запуск бекенда
poetry run uvicorn app.src.main:app --reload --port 8000 --host 0.0.0.0
### Дока с методами будет доступна на 
### http://0.0.0.0:8000/balance-api/docs
```