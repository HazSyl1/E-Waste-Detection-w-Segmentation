import cv2 as cv
from ultralytics import YOLO
from google.colab.patches import cv2_imshow
def detect(image):
  model = YOLO('yolov8n.pt')
  model = YOLO('/content/runs/detect/eWaste2/weights/best.pt')

  results = model.predict(image)

  image = cv.imread(image)
  for box in results[0].boxes:
    class_id = results[0].names[box.cls[0].item()]
    cords = box.xyxy[0].tolist()
    cords = [round(x) for x in cords]
    conf = round(box.conf[0].item(), 2)
    x1, y1, x2, y2 = cords
    color = (0, 0, 255)  
    thickness = 2
    cv.rectangle(image, (x1, y1), (x2, y2), color, thickness)
    text = f'Object: {class_id} --- Confidence: {conf}'
    cv.putText(image, text, (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

  cv2_imshow(image)
  # cv.imshow(image)
  # cv.waitKey(0)
  # cv.destroyAllWindows()

