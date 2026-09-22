from fastapi import FastAPI
from api.routes import user_route

app = FastAPI(title="Todo Backend API")

app.include_router(user_route.router, prefix="/api/routes/users", tags=["Users"])

@app.get("/health")
def health():
    return {"response": "Backend is working..."}