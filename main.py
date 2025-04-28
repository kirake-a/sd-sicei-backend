from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from infrastructure.api.student_router import router as student_router
from infrastructure.api.subject_router import router as subject_router
from infrastructure.api.grade_router import router as grade_router

from infrastructure.db.database import engine
from infrastructure.db.models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(student_router)
app.include_router(subject_router)
app.include_router(grade_router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="SICEI API",
        version="1.0.0",
        summary="Summary of the API",
        description="Description of the API",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
