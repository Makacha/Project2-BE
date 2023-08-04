from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.helpers.exception_type import ExceptionType
from app.schemas.exception_schemas import AppException
from app.schemas.response_schemas import ResponseBase


def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.http_code,
        content=jsonable_encoder(ResponseBase().fail_response(exc.code, exc.message))
    )


def exception_handler(request: Request, exc):
    return JSONResponse(
        status_code=ExceptionType.INTERNAL_SERVER_ERROR.http_code,
        content=jsonable_encoder(ResponseBase().fail_response(ExceptionType.INTERNAL_SERVER_ERROR.code,
                                                              ExceptionType.INTERNAL_SERVER_ERROR.message))
    )
