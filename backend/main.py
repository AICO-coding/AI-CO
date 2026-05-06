# FastAPI 앱 생성, 라우터 등록
from fastapi import FastAPI
from app.routers.authRouters import router as auth_router
from app.routers.userRouters import router as user_router
from app.routers.chatRouters import router as chat_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(chat_router)