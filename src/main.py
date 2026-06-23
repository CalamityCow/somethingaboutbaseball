import cv2
def main():
 cap = cv2.VideoCapture(0)

 if not cap.isOpened():
  print("Camera failed to open")
  return

 while True:
  ret, frame = cap.read()

  if not ret:
   print("Failed to read frame")
   break

  cv2.imshow("Baseball Tracker", frame)

  key = cv2.waitKey(1) & 0xFF
  if key == 27:  # escape key
   break

 cap.release()
 cv2.destroyAllWindows()

if __name__ == "__main__":
 main()
