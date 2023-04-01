from fastapi import FastAPI
from application.routers import users, login,item, home
from core.contracts import models
from core.service import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(home.router)
app.include_router(login.router)
app.include_router(users.router)
app.include_router(item.router)

