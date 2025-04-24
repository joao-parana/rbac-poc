import uvicorn
import time
import threading
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from rbac_poc.main import RbacPoc


rest_api = FastAPI()

# Montar o diretório estático
rest_api.mount("/static", StaticFiles(directory="static"), name="static")

def run_uvicorn(port: int):
    # uvicorn.run("your_app:rest_api", host="0.0.0.0", port=8080)
    uvicorn.run(rest_api, host="0.0.0.0", port=port)  # noqa S104

def main():
    rbac_poc = RbacPoc(rest_api)
    rbac_poc.define_rest_api_endpoints()
    thread_name = f"_run_uvicorn_thread-{len(threading.enumerate())}"
    uvicorn_port = 8093
    t = threading.Thread(target=run_uvicorn, args=(uvicorn_port,), name=thread_name)
    t.start()
    print("Servidor uvicorn rodando em uma thread separada.", flush=True)
    while True:
        time.sleep(5)

if __name__ == "__main__":
    main()
