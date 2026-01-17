import cv2
from ultralytics import YOLO
import os

# Paths
VIDEO_PATH = "../videos/traffic.mp4"
# MODEL_PATH = "../models/yolov8n.pt"

# Load model
#model = YOLO(MODEL_PATH)
model = YOLO("yolov8n.pt")


# Open video
cap = cv2.VideoCapture(VIDEO_PATH)

vehicle_classes = ["car", "motorcycle", "bus", "truck"]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, stream=True)
    vehicle_count = 0

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            class_name = model.names[cls_id]

            if class_name in vehicle_classes:
                vehicle_count += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(frame, (x1, y1), (x2, y2),
                              (0, 255, 0), 2)
                cv2.putText(frame, class_name,
                            (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 255, 0), 2)

    cv2.putText(frame, f"Vehicle Count: {vehicle_count}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

    cv2.imshow("AI Smart Traffic Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
