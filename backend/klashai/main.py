from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from klashai.config import settings
from klashai.routers.health import router as health_router
from klashai.utils.logging import setup_logging

setup_logging()

app = FastAPI(
    title="KlashAI API",
    description="Next-generation AI platform for gaming, coding, and productivity.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health_router, prefix="/api/v1", tags=["health"])


@app.get("/")
async def root():
    return {"message": "Welcome to KlashAI API"}
