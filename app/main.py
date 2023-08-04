from fastapi import FastAPI
from app.apis import apis
from app.helpers.exception_handler import app_exception_handler, exception_handler
from app.schemas.exception_schemas import AppException
from fastapi.middleware.cors import CORSMiddleware

from uvicorn import run

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
app.include_router(apis.router)
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, exception_handler)

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
