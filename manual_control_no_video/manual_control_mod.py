from djitellopy import Tello
import cv2, math, time
import threading


end = False

def display_video():
    while True and (not end):
        img = frame_read.frame
        cv2.imshow("drone", img)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()



# Create a new thread for displaying the video
video_thread = threading.Thread(target=display_video)
video_thread.start()
   
    


while True:
    key = cv2.waitKey(1) & 0xff
    if key == 27:  # ESC
        break
    elif key == ord('w'):
        tello.move_forward(30)
    elif key == ord('s'):
        tello.move_back(30)
    elif key == ord('a'):
        tello.move_left(30)
    elif key == ord('d'):
        tello.move_right(30)
    elif key == ord('e'):
        tello.rotate_clockwise(30)
    elif key == ord('q'):
        tello.rotate_counter_clockwise(30)
    elif key == ord('r'):
        tello.move_up(30)
    elif key == ord('f'):
        tello.move_down(30)
    elif key == ord('t'):
        tello.takeoff()
    elif key == ord('l'):
        tello.land()

tello.land()
