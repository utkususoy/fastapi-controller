#
#
# import uvicorn
#
# import concurrent.futures
#
# app = FastAPI()
#
#
#
# # Sample data store
# items = []
#
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, workers=4)
from controller.controller import Controller

app = Controller()