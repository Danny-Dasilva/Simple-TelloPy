
from time import sleep
import tellopy
import time
import sys
import pygame
import threading
import av
import cv2 as cv2 
import numpy
import traceback



prev_flight_data = None
run_recv_thread = True
new_image = None
flight_data = None
log_data = None
buttons = None

def handler(event, sender, data, **args):
    global prev_flight_data
    global flight_data
    global log_data
    
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        if prev_flight_data != str(data):
            print(data)
            prev_flight_data = str(data)
        flight_data = data
    elif event is drone.EVENT_LOG_DATA:
        log_data = data
    else:
        print('event="%s" data=%s' % (event.getname(), str(data)))

def draw_text(image, text, row):
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        font_size = 24
        font_color = (255,255,255)
        bg_color = (0,0,0)
        d = 2
        height, width = image.shape[:2]
        left_mergin = 10
        if row < 0:
            pos =  (left_mergin, height + font_size * row + 1)
        else:
            pos =  (left_mergin, font_size * (row + 1))
        cv2.putText(image, text, pos, font, font_scale, bg_color, 6)
        cv2.putText(image, text, pos, font, font_scale, font_color, 1)



def recv_thread(drone):
    global run_recv_thread
    global new_image
    global flight_data

    print('start recv_thread()')
    try:
        container = av.open(drone.get_video_stream())
        # skip first 300 frames
        frame_skip = 300
        while True:
            for frame in container.decode(video=0):
                if 0 < frame_skip:
                    frame_skip = frame_skip - 1
                    continue
                start_time = time.time()
                image = cv2.cvtColor(numpy.array(frame.to_image()), cv2.COLOR_RGB2BGR)

                if flight_data:
                    draw_text(image, 'TelloPy: joystick_and_video ' + str(flight_data), 0)
                new_image = image
                if frame.time_base < 1.0/60:
                    time_base = 1.0/60
                else:
                    time_base = frame.time_base
                frame_skip = int((time.time() - start_time)/time_base)
    except Exception as ex:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        print(ex)

    
class Drone():
    def __init__(self):
        self.drone = tellopy.Tello()
        self.drone.connect()
        self.drone.subscribe(self.drone.EVENT_FLIGHT_DATA, handler)
        self.drone.subscribe(self.drone.EVENT_LOG_DATA, handler)
        self.current_image = None
    
    def counter_clockwise(self, speed):
        self.drone.counter_clockwise(speed)
    def clockwise(self, speed):
        self.drone.clockwise(speed)
    def forward(self, speed):
        self.drone.forward(speed)
    def backward(self, speed):
        self.drone.backward(speed)
    def left(self, speed):
        self.drone.left(speed)
    def right(self, speed):
        self.drone.right(speed)
    def up(self, speed):
        self.drone.up(speed)
    def down(self, speed):
        self.drone.down(speed)
        
    def takeoff(self):
        time.sleep(.5)
        self.drone.takeoff()
    def land(self):
        time.sleep(.5)
        self.drone.land()
    def sleep(self, sec):
        print("before")
        time.sleep(sec)
        print("after")
        self.drone.counter_clockwise(0)
        self.drone.clockwise(0)
        self.drone.forward(0)
        self.drone.backward(0)
        self.drone.left(0)
        self.drone.right(0)
        self.drone.up(0)
        self.drone.down(0)
    def video(self):
        global buttons
        global run_recv_thread
        global new_image
        
        threading.Thread(target=recv_thread, args=[self.drone]).start()

        try:
            while 1:
                # loop with pygame.event.get() is too much tight w/o some sleep
                time.sleep(0.02)    
                if self.current_image is not new_image:
                    cv2.imshow('Tello', new_image)
                    self.current_image = new_image
                    cv2.waitKey(1)
        except KeyboardInterrupt as e:
            print(e)
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback)
            print("error", e)
