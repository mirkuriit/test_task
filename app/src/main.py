from fastapi import FastAPI
from app.config import config


from app.src.routers.balance_router import router as balance_router
print(config.URL_PREFIX)
app = FastAPI(docs_url=f'{config.URL_PREFIX}/docs',)

app.include_router(balance_router)