# Bangla Sign Language Detection using **YOLO v10** 

##  Overview  
This project uses **YOLO v10** for real-time Bangla Sign Language (BdSL) detection. It is trained on the **KU-BdSL** and **BdSL47** datasets, which contain various hand gestures used in Bangla Sign Language.  
Both datasets are open sounce & free to use for research purposes.
---

##  Features  
✅ **YOLO v10-based real-time detection**  
✅ **Trained on open-source BdSL datasets**  
✅ **Supports image, video, and webcam input**  
✅ **Optimized for speed & accuracy**  

---

## Dataset  
- **[KU-BdSL Dataset]([https://data.mendeley.com/datasets/scpvm2nbkm/4])** – A dataset for Bangla sign language gestures.  
- **[BdSL47 Dataset]([https://zenodo.org/records/7067906])** – A dataset containing 47 Bangla sign language classes.  

---

## Model Training
To train the YOLO v10 model on your dataset:

```bash
yolo train model=yolov10n.pt data=dataset.yaml epochs=100 imgsz=640 batch=32 device=0 patiences=3
```
📌 Options:

- model=yolov10n.pt → Use YOLOv10 Nano (lightweight model)
- data=dataset.yaml → Path to dataset YAML file
- epochs=100 → Number of training epochs
- imgsz=640 → Image size
- batch=16 → Batch size
- device=0 → Use GPU (if available)

## Detect from an Image
```bash
yolo task=detect mode=predict model=best.pt source=sample.jpg
```
Options:

- task=detect → Runs object detection
- mode=predict → Uses the trained model for predictions
- model=best.pt → Path to the trained model
- source=0 → Uses webcam (or specify an image/video file)

## Trainging Result : 
- mAP50 : 0.99241

