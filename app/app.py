from fastapi import FastAPI
from fastapi.responses import HTMLResponse 
from app.routers.model import model_router


app = FastAPI()

app.include_router(model_router)

@app.get('/home', tags = ['home'])
def home():
    return HTMLResponse("<h1>Welcome</h1>")