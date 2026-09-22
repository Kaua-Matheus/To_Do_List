from fastapi import FastAPI
from api.routes import user_route


app = FastAPI(title="Todo Backend API", version="0.0.1")

app.include_router(user_route.router, prefix="/api", tags=["Users"])

@app.get("/health")
def health():
    return {"response": "Backend is working..."}