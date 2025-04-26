# Debug using dockerfiles

the goal of the project is jus to set up python fastapi **breakpoint** debug experience inside **containers** using **vscode**.
This has been created in windows/powershell environment. 

 - create python virtual environment
	 - `python3 -m venv .venv`
 - activate virtual environment
	 - `.\.venv\Scripts\activate`
 - add the following dependency in your requirements.txt file : 
	 - debugpy
	 - git+https://github.com/re7w12u/pdebugger.git
		 *- you might want to clone de repo in case you need to make some change, port number for instance.*
 		 *- it's possible to use the following url instead if you need more verbose debugger initialization : git+https://github.com/re7w12u/pdebugger.git@dev*
		 
 - install dependencies
	 - `python -m pip install -r requirements.txt`
 - create debug configuration in vscode launch.json file
	```json
	{
	      "name": "Python Debugger: Remote Attach",
	      "type": "debugpy",
	      "request": "attach",
	      "connect": {
	        "host": "localhost",
	        "port": 5978
	      },
	      "pathMappings": [
	        {
	          "localRoot": "${workspaceFolder}",
	          "remoteRoot": "/app"
	        }
	      ] 
	}
	```
- add following lines in main.py, where the app is initialized
```python 
 from  debugger  import initialize_debugger_if_needed
```
```python
 initialize_debugger_if_needed()
``` 

- As an example :
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pdebugger.pdebugger import initialize_debugger_if_needed

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
initialize_debugger_if_needed()
		
@app.get("/")
async def root():
    return {"message": "Hello World from product service!"}
```
- How it works :
	- the `initialize_debugger_if_needed()` function basically checks :
		- if an environment variable (called DEBUGGER, see below) is set to True
		- triggers debugpy listening on specific port
		- waits for vscode debugger to be attached (using F5)
 
- Now, run the container you want to debug using the following command :
	- `docker run --rm -p 8002:8002 -p 5978:5978 -d -e DEBUGGER=True -e DEBUGGER_PORT=5978 msvc-user:0.1`
		- port 8002 is the port of the fastapi application
		- port 5978 is used to attach the debugger
		- DEBUGGER environment variable is used to trigger debugging (or not)
		- DEBUGGER_PORT environment variable must match the second -p option value
	- Go to vscode and press F5 (or run the matching configuration using the menu)
	 
# Debug using docker compose
it's basically the same principals as described above.
The difference is that it's all wrapped in a docker compose files which can be steered from makefile commands.
- docker files 
	- `docker-compose.yaml` run the containers in standard (no debug) mode
 	- `docker-compose-debug.yaml` run the containers in debug mode

That being said and unless specific needs, you should only deal with the makefile commands.
- install make (if not present)
- I think instructions and comments are pretty self explantory 


```r
dc:=docker-compose.yaml
dc-debug:=docker-compose-debug.yaml

# build docker containers for the project.
build:
	docker compose -f $(dc) build

# build docker containers for the project with no cache
build-no-cache:
	docker compose -f $(dc) build --no-cache

# runs containers
up:
	docker compose -f $(dc) up -d

#stops containers
down:
	docker compose -f $(dc) down

# run all containers in debug mode
debug-up:
	docker compose -f $(dc-debug) up

# stop msvc-user service and run only msvc-user in debug mode
debug-user-up: user-down
	docker compose -f $(dc-debug) up -d msvc-user

# stop msvc-product service and run only msvc-product in debug mode
debug-product-up: product-down
	docker compose -f $(dc-debug) up -d msvc-product

# stop msvc-product service
product-down:
	docker compose -f $(dc-debug) down msvc-product

# stop msvc-user service
user-down:
	docker compose -f $(dc-debug) down msvc-user
```