import os

from fastapi import APIRouter, FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount(
    '/static',
    StaticFiles(directory=os.path.join(os.getcwd(), 'static')),
    name='static',
)

templates = Jinja2Templates(directory='templates')

homepage_router = APIRouter(tags=['Tracker API'])


@homepage_router.get('/', response_class=HTMLResponse)
async def index(request: Request):
    """
    Serve a página principal do projeto, retorna um HTML Response.

    """
    return templates.TemplateResponse('index.html', {'request': request})


# @app.get('/todos', response_class=HTMLResponse)
# async def list_todos(
#     request: Request, hx_request: Annotated[Union[str, None], Header()] = None  # noqa: E501
# ):
#     if hx_request:
#         return templates.TemplateResponse(
#             request=request, name='todos.html', context={'todos': todos}
#         )


#     jsonable_todos = jsonable_encoder(todos)
#     return JSONResponse(jsonable_todos)


app.include_router(homepage_router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title='CV Tracker API',
        version='1.0.0',
        description='API documentation for CV Tracker application',
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
