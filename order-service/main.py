from fastapi import FastAPI

app = FastAPI(title="Order Service")

@app.get("/orders")
def get_orders():
    return [{"order_id": 101, "user_id": 1, "amount": 500}]
