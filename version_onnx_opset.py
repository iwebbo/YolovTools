import onnx
model = onnx.load("best.onnx")
print(model.opset_import[0].version)