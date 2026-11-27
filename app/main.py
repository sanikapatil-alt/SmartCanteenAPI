
from fastapi import FastAPI
from app.routes import menu, orders

app = FastAPI(
    title="Smart Canteen Ordering API",
    description="API for managing canteen menu, orders and billing",
    version="1.0.0"
)

app.include_router(menu.router)
app.include_router(orders.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Canteen Ordering System",
        "status": "Application is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
