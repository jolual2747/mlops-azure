from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse 
from app.routers.model import model_router


app = FastAPI()

app.include_router(model_router)

@app.get('/home', tags = ['home'], response_model=HTMLResponse)
def home():
    return HTMLResponse("<h1>Welcome</h1>")

@app.get('/ping', tags = ['home'])
def ping():
    return JSONResponse(content={"message":"pong"}, status_code=200)