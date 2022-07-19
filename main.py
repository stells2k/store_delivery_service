"""Main file for delivery service"""
import uvicorn

from fastapi import FastAPI
from src.app.routers import routers

app = FastAPI(title='delivery-service',
              docs_url='/delivery-service/docs',
              openapi_url='/delivery-service',
              debug=True
              )

app.include_router(routers, prefix='/delivery-service')


@app.get("/", tags=["Root"])
async def read_root():
    '''Just welcome message'''
    return {"message": "Welcome to delivery-service app!"}


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        'main:app',
        workers=1,
        reload=True,
    )


if __name__ == "__main__":
    main()
