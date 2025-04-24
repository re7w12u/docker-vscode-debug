import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from debugger import initialize_flask_server_debugger_if_needed

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
print("running msvc-user service")
initialize_flask_server_debugger_if_needed()

@app.get("/")
async def root():
    return {"message": "Hello World from user service!"}