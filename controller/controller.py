from fastapi import FastAPI, HTTPException
import time
import threading

class Controller(FastAPI):
    def __init__(self):
        super(Controller, self).__init__()

        def inf_loop():
            while True:
                time.sleep(1)
                print("inf loop running.")

        @self.on_event("startup")
        async def startup_event():
            run_inf_loop()

        def run_inf_loop():
            thread = threading.Thread(target=inf_loop)
            thread.start()

        @self.get("/hello")
        async def hello_world():
            return {"response": "Hello World!"}


