# dev_run.py
from frontend.ui import create_ui
from backend.services.inference import predict

iface = create_ui(fn=predict)
iface.launch()
