import os

from fastapi import FastAPI, Request
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


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')


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
