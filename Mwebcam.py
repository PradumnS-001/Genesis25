import cv2
# To start the camera
cap = cv2.VideoCapture(0)
# Here we insert 0 because we are using the inbuilt webcam. Instead, if we want to use an external webcam, we have to replace 0 by 1

while True:
    # To capture a frame since video is nothing but images one after another
    _, frame = cap.read()
    # Displaying the video as images
    cv2.imshow('show video', frame)
    # To exit program at a specific key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 