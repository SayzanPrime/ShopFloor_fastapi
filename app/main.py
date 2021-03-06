import asyncio
from random import randint
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from .utils.const import description

# Initializing fastapi

app = FastAPI(
    title="Websocket Code Example",
    description=description,
)

# Cors configuration
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Api endpoints 
@app.get('/')
def home():
    return {'Welcome to the api... access api docs with => /docs'}

# Websocket 
@app.websocket('/ws/chart')
async def chartWs(websocket: WebSocket):
    await websocket.accept()
    await websocket.receive_text()

    listX = [i for i in range(50)]
    listY = [randint(1,100) for i in range(50)]
    while True:
        try:
            listX.append(listX[len(listX)-1] + 1)
            listX.pop(0)

            listY.append(randint(1,100))
            listY.pop(0)
            await websocket.send_json({
                "listX": listX,
                "listY": listY
            })
        except Exception as e:
            print('error:', e)
            break
        await asyncio.sleep(0.09) 
