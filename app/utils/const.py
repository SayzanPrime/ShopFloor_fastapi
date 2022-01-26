# This modules contain constant variables

description = """

## Environment.ts : 

export const environment = { \n
  &emsp; production : false, \n
  &emsp; APIUrl : 'http://localhost:8000/', \n
  &emsp; **WSUrl : 'ws://localhost:8000/ws/'** \n
};

---------------------------------------------

## Component.ts :

\timport { webSocket } from "rxjs/webSocket";


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

