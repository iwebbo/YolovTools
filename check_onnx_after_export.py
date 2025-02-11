import onnx

model_path = "best.onnx"  # Mets le bon chemin
onnx_model = onnx.load(model_path)
onnx.checker.check_model(onnx_model)
print("✅ Modèle ONNX valide.")

model = onnx.load("best.onnx")
for input in model.graph.input:
    print(f"Nom de l'entrée : {input.name}")
    for dim in input.type.tensor_type.shape.dim:
        print(dim.dim_value)

model = onnx.load("best.onnx")
print(f"Opset version: {model.opset_import[0].version}")