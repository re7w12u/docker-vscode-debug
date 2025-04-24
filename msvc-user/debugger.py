from os import getenv

def initialize_debugger_if_needed():
    print("initialize_flask_server_debugger_if_needed() called")
    print("DEBUGGER:", getenv("DEBUGGER"))
    if getenv("DEBUGGER") == "true":
        import multiprocessing
        print(f'multiprocessing = {multiprocessing.current_process().pid}')
        if multiprocessing.current_process().pid >= 1:
            import debugpy
            print("👾 Attaching debugger 👾", flush=True)
            debugpy.listen(("0.0.0.0", 5978))
            print("⏳ VS Code debugger can now be attached, press F5 in VS Code ⏳", flush=True)
            debugpy.wait_for_client()
            print("🎉 VS Code debugger attached, enjoy debugging 🎉", flush=True)