import uvicorn as uvicorn

from app.endpoints.routes import add_new_route
app = add_new_route()

if __name__ == "__main__":
    uvicorn.run(
        'app:app',
        # host=Config.fastapi_host,
        # port=Config.fastapi_port,
        # ssl_keyfile="certs/local.key",
        # ssl_certfile="certs/local.pem",
        # workers=Config.workers,
        reload=True
    )