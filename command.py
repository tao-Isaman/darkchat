from typing import List

from fastapi import WebSocket

class Room:
    def __init__(self,name):
        self.name = name
        self.user: List[WebSocket] = []
    
    def join_room(self, websocket: WebSocket):
        self.user.append(websocket)



# manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.roomList: List[Room] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def user_join_room(self, websocket: WebSocket , client_id):
        for connection in self.active_connections:
            if websocket != connection:
                await connection.send_text(f'User {client_id} has join this room ') 

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str, yourId: WebSocket):
        for connection in self.active_connections:
            if yourId != connection:
                await connection.send_text(message) 

    async def create_room(self, name: str , websocket: WebSocket):
        newRoom = Room(name)
        newRoom.join_room(websocket)
        self.roomList.append(newRoom)
        await websocket.send_text(f'room {name} has created')

    async def get_list_room(self, websocket: WebSocket):
        for room in self.roomList:
            await websocket.send_text(room.name)


manager = ConnectionManager()