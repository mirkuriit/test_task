```commandline
git clone git@github.com:mirkuriit/test_task.git
cd test_task
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