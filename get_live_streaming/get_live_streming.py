from djitellopy import Tello
import cv2

# Create a Tello object
tello = Tello()

# Connect to Tello
tello.connect()

# Start the video stream
tello.streamon()

# Create a GUI window
cv2.namedWindow('Tello Video', cv2.WINDOW_NORMAL)

while True:
    # Read a frame from the video stream
    frame = tello.get_frame_read().frame

    # Display the frame in the GUI window
    cv2.imshow('Tello Video', frame)

    # Check for key presses
    key = cv2.waitKey(1) & 0xff
    if key == 27: # Escape key
        break

# Stop the video stream
tello.streamoff()

# Disconnect from Tello
tello.disconnect()

# Close the GUI window
cv2.destroyAllWindows()