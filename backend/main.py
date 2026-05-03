# FastAPI 앱 생성, 라우터 등록
from fastapi import FastAPI
from app.routers.chatRouters import router as chat_router

app = FastAPI()

app.include_router(chat_router)