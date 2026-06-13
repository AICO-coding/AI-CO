from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers.authRouters import router as auth_router
from app.routers.userRouters import router as user_router
from app.routers.chatRouters import router as chat_router
from app.routers.noteRouters import router as note_router
from app.routers.lessonRouters import router as lesson_router
from app.routers.dailyRouters import router as daliy_router
from app.routers.reportRouters import router as report_router
from app.routers.missionRouters import router as mission_router
from fastapi.middleware.cors import CORSMiddleware
from app.services.chatbot.indexer import build_index


@asynccontextmanager
async def lifespan(app: FastAPI):
    build_index()
    yield


app = FastAPI(lifespan=lifespan)

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
app.include_router(daliy_router)
app.include_router(report_router)
app.include_router(mission_router, prefix="/mission", tags=["mission"])