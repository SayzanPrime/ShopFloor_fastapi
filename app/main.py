import asyncio
import json
from random import randint
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

# Initializing fastapi

description = """

## Environment.ts : 

export const environment = { \n
  &emsp; production : false, \n
  &emsp; APIUrl : 'http://localhost:8000/', \n
  &emsp; **WSUrl : 'ws://localhost:8000/ws/'** \n
};

---------------------------------------------

## Component.ts :

\treadonly WSUrl = environment.WSUrl;

\tchart_data : any;

\tngOnInit(): void {

\tthis.connectToWs();
\t}

\tconnectToWs(){ 

        const chart_ws = webSocket(this.WSUrl + 'chart')

        chart_ws.next({message: 'Connected To Client Via WebSockets'});

        chart_ws.subscribe(
            msg => this.chart_data = msg, // Called whenever there is a message from the server.
            err => console.log(err), // Called if at any point WebSocket API signals some kind of error.
            () => console.log('complete') // Called when connection is closed (for whatever reason).
        );
    }
"""


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

    random_list = [randint(10,50) for i in range(8)]
    while True:
        try:
            random_list.append(randint(10,50))
            await websocket.send_json(random_list[1:])
        except Exception as e:
            print('error:', e)
            break
        await asyncio.sleep(1) 
