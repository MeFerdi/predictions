from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import airquality

app = FastAPI(title="Air Quality Insights API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(airquality.router, prefix="/api/airquality", tags=["airquality"])

@app.get("/api/health")
async def health():
    return {"status": "ok"}
