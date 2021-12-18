from fastapi import (
    FastAPI, WebSocket, WebSocketDisconnect,
    Request, Response
)
from typing import List
from pydantic import BaseModel

from fastapi.templating import Jinja2Templates
from command import manager

# locate templates
templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    await manager.user_join_room(websocket, client_id)
    try:
        while True:
            data = await websocket.receive()
            print(data)
            if 'text' in data:
                text = data['text']
            else :
                text = data['bytes'].decode('UTF-8')
                
            await command(text, websocket, client_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat", client_id)

async def command(message: str , websocket: WebSocket , client_id: int):
    command = message.split(' ')
    print(command)
    if (command[0][0] != '/'):
        await manager.send_personal_message(f"Your : {message}" , websocket)
        await manager.broadcast(f"User #{client_id} : {message}", websocket)
    if (command[0] == '/roomlist'):
        await manager.get_list_room(websocket)
    
    if(command[0] == '/createroom'):
        await manager.create_room(command[1], websocket)
    
