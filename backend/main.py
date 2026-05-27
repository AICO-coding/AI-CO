# FastAPI 앱 생성, 라우터 등록
from fastapi import FastAPI
from app.routers.authRouters import router as auth_router
from app.routers.userRouters import router as user_router
from app.routers.chatRouters import router as chat_router
from app.routers.noteRouters import router as note_router
from app.routers.lessonRouters import router as lesson_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(chat_router)
app.include_router(note_router)
app.include_router(lesson_router)