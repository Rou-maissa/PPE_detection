from ultralytics import YOLO
import cv2

model = YOLO(r"C:\Users\pc\Desktop\model\ppee\best.pt")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.3)

    person_detected = False
    helmet_detected = False
    no_helmet_detected = False

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls].lower()
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, label, (x1, y1-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

            if label == "person":
                person_detected = True
            elif label == "helmet":
                helmet_detected = True
            elif label == "no_helmet":
                no_helmet_detected = True

    # PPE decision
    if person_detected:
        if helmet_detected and not no_helmet_detected:
            text, color = "PPE OK", (0,255,0)
        else:
            text, color = "PPE NOT OK", (0,0,255)

        cv2.putText(frame, text, (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    cv2.imshow("PPE Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
