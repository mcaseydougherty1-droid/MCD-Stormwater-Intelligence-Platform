from fastapi import FastAPI

from mcd.api.routers.properties import router as properties_router

app = FastAPI(
    title="MCD Stormwater Intelligence Platform",
    version="2.3.1",
    description="API backend for stormwater property intelligence, CRM, inspections, and asset management.",
)

app.include_router(properties_router)


@app.get("/")
def root():
    return {
        "status": "ok",
        "platform": "MCD Stormwater Intelligence Platform",
        "version": "2.3.1",
    }
