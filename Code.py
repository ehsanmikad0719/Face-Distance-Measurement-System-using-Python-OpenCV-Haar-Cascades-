# Importing OpenCV library
import cv2

# Average physical width of an adult human face (cm)
REAL_FACE_WIDTH = 14.0
# Focal length (pixel): Formula of FOCAL_LENGTH_PIXEL = (face_width_pixel*Distance_from_camera)/REAL_FACE_WIDTH
FOCAL_LENGTH_PIXEL = 750.0

# Load the Haar Cascade classifier 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open the webcam for live video feed
web = cv2.VideoCapture(0)

while True:
    ret, frame = web.read()
    if not ret:
        break
    # Convert Frame to Grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Face Detect
    face = face_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 10,
        minSize = (30,30)
    )

    # Draw Rectangle around detected face
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        # Width of face in pixel
        face_width_pixel = w

        # Distance 
        distance = (REAL_FACE_WIDTH*FOCAL_LENGTH_PIXEL)/face_width_pixel

        # Displaying the calculated distance
        cv2.putText(frame, f"Distance:{distance} cm", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0),2)

    # Output
    cv2.imshow("Face with eye Detection System", frame)

    # Press 'q' to stop taking feed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
# Release the video feed
web.release()
cv2.destroyAllWindows()
