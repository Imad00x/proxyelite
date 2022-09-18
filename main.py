# main.py
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/",response_class=PlainTextResponse)
def hello():
    return 'hello world'

