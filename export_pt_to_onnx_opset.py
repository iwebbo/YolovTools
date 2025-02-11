from ultralytics import YOLO

# Charger ton modèle YOLOv8 entraîné
model = YOLO("best.pt")  # Mets ici le bon chemin vers ton modèle

# Exporter en ONNX avec opset 12 (supporté par OpenCV)
model.export(format="onnx", opset=12)

print("✅ Modèle YOLOv8 exporté en ONNX avec opset=12.")