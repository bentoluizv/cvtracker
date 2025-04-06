import os

from fastapi import APIRouter, FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from cvtracker.settings import get_settings

settings = get_settings()

app = FastAPI()

app.mount(
    '/static',
    StaticFiles(directory=os.path.join(os.getcwd(), 'static')),
    name='static',
)

templates = Jinja2Templates(directory='templates')

pages_router = APIRouter(tags=['Pages'])
api_router = APIRouter(prefix='/api/v1', tags=['API'])


@pages_router.get('/', response_class=HTMLResponse)
async def index(request: Request):
    """
    Serve a página principal do projeto, retorna um HTML Response.

    """
    return templates.TemplateResponse('index.html', {'request': request})


@api_router.get('/', response_class=JSONResponse)
async def api_index():
    """
    Página inicial da API, retorna um JSON Response.
    Essa rota pode ser usada para verificar se a API está funcionando
    corretamente, seu status e outras informações relevantes.

    """
    return JSONResponse({
        'description': 'API para o aplicativo TrackerCV',
        'version': settings.API_VERSION,
        'api': '/api/v1',
        'docs': '/docs',
        'redoc': '/redoc',
        'env': settings.ENVIROMENT,
    })


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


app.include_router(pages_router)
app.include_router(api_router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title='Documentação - TrackerCV',  # Título da documentação
        version='1.0.0',  # Versão da API
        description=(
            'Esta é a documentação da API para o aplicativo TrackerCV, '
            'uma aplicação desenvolvida para rastrear e gerenciar currículos. '
            'Aqui você encontrará detalhes sobre os endpoints disponíveis, '
            'os métodos HTTP suportados e os parâmetros necessários.'
        ),
        routes=app.routes,  # Rotas registradas na aplicação
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
