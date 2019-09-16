"""
Example commands for Tello:
forward
backward
left
right
up
down
clockwise
counter_clockwise

Created for Tech Garage
Contributors: Dexter Dixon, Danny Dasilva
"""



from app.Drone import Drone

drone = Drone()



drone.takeoff()

drone.sleep(2)
drone.counter_clockwise(30)
drone.sleep(2)
drone.clockwise(30)
drone.sleep(3)


drone.land()