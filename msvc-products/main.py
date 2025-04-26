import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pdebugger.pdebugger import initialize_debugger_if_needed

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
print("starting debugger 1")
initialize_debugger_if_needed()
print("starting debugger 2")
@app.get("/")
async def root():
    current_time = datetime.datetime.now().isoformat()
    return {"message": f"Hello World from product service! Current Time: {current_time}"}    