from fastapi import FastAPI
from backend.services.inference import predict
from frontend.ui import create_ui

app = FastAPI()

# FastAPI route for prediction
@app.post("/predict/")
async def get_prediction(data: dict):
    return predict(data)

# Gradio UI setup
iface = create_ui(fn=predict)

if __name__ == "__main__":
    iface.launch()
