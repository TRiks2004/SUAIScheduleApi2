from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from logger.logger import get_list_logs, get_log_file
from datetime import datetime, timedelta


logs_router = APIRouter(
    prefix="/logs",
    tags=["Logs"],
)


templates_handler_log = Jinja2Templates(directory="templates")



@logs_router.get("/")
async def get_logs()-> list[dict]:
    return await get_list_logs()

@logs_router.get("/{name}")
async def get_log(name: str = 'log.json') -> dict:
    return await get_log_file(name)

@logs_router.get("/{name}/page")
async def get_log(request: Request, name: str = 'log.json', ):
    
    log_file = await get_log_file(name)

    for i in log_file['body']:
        item = i['record']['level']
        match item['name']:
            case 'DEBUG':
                item['color'] = '#80fc68'
            case 'INFO':
                item['color'] = '#51e3fc'
            case 'WARNING':
                item['color'] = '#eded4e'
            case 'ERROR':
                item['color'] = '#ed7461'
            case 'CRITICAL':
                item['color'] = '#f23a90'


    return templates_handler_log.TemplateResponse('templates_handler_log.html', {'request': request, 'name': name, 'log_file': log_file})

