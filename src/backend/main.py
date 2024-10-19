
import uvicorn
from fastapi import FastAPI, Body, Path, Query
from src.backend.routers import openings_router

app = FastAPI()
app.include_router(openings_router.router)


if __name__ == "__main__":
    uvicorn.run("src.backend.main:app", host="0.0.0.0", port=3030, reload=False, log_level="debug")