import cv2
import numpy as np
from djitellopy import Tello

# Connect to Tello
tello = Tello()
tello.connect()

# Set up video stream
tello.streamon()
frame = tello.get_frame_read()

# Set up video writer
video_out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 30, (960, 720))

while True:
    # Get the latest frame from the video stream
    img = frame.frame

    # Display the frame in a window
    cv2.imshow('Tello', img)

    # Write the frame to the video file
    video_out.write(img)

    # Check for key presses
    key = cv2.waitKey(1) & 0xff
    if key == ord('q'):
        break

# Release the video writer and video stream
video_out.release()
cv2.destroyAllWindows()
tello.streamoff()
tello.end()