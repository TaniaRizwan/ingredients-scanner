import cv2

# Try to open your default webcam (0 = first camera)
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    raise SystemExit("⚠️ Could not access camera. Make sure it's not in use by other applications.")

print("Press SPACE to capture, or q to quit.")

while True:
    ok, frame = cap.read()
    if not ok:
        continue

    cv2.imshow("Camera Test", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord(' '):  # SPACE
        cv2.imwrite("test_capture.png", frame)
        print("✅ Saved frame as test_capture.png")
        break
    elif key in (ord('q'), 27):  # q or ESC
        print("❌ Quit without saving")
        break

cap.release()
cv2.destroyAllWindows()
