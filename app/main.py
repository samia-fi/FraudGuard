from fastapi import FastAPI
from app.api.transactions import router as transactions_router
from app.api.merchants import router as merchants_router
app = FastAPI(
    title="FraudGuard API",
    description="Real-time fraud detection platform",
    version="1.0.0",
)

app.include_router(transactions_router)
app.include_router(merchants_router)


@app.get("/")
def home():
    return {"message": "Welcome to FraudGuard API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}