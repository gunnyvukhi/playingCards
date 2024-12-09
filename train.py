from ultralytics import YOLO

model = YOLO("playingCards.pt")  # load a pretrained model
# Train the model
results = model.train(data="TrainingData\data.yaml", epochs=100, imgsz=640)