# README : YolovTools

#### ENGLISH VERSION 

## Technologies 

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) ![Yolov](https://img.shields.io/badge/Yolov-FCC624?style=for-the-badge&logo=Yolov&logoColor=black) ![ONNX](https://img.shields.io/badge/ONNX-3776AB?style=for-the-badge&logo=ONNX&logoColor=white) 

## 📌 Prerequisites
### 🖥 Hardware:

A computer capable of running Python.
### 🛠 Run IT:

Export your model training PT to ONNX Format.
Before to run, change the name of your model.

```
python export_pt_to_onnx_opset.py
```

Check the format after the export 

```
python check_onnx_after_export.py
```
For example :

```
✅ Model ONNX valid.
Name of entry : images
1
3
640
640
Opset version: 19 --> Most of the case, Opset 19 can be make some issue. 
```

