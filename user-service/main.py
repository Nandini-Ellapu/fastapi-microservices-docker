from fastapi import FastAPI

app = FastAPI(title="User Service")

@app.get("/users")
def get_users():
    return {"message": "Users list returned successfully"}
