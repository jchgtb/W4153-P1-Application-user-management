from fastapi import Depends, FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.routers import users_router, flights_router, login_router, matching_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)
app.add_middleware(SessionMiddleware, secret_key="root")

app.include_router(users_router.router)
app.include_router(flights_router.router)
app.include_router(login_router.router)
app.include_router(matching_router.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, reload=True)



