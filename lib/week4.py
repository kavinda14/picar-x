import time
import sys
import concurrent.futures
import threading
from interpreter import Interpretation
from sensor import Sensor
from controller import Controller
from bus import Busses
        
def Consumers(consumerbusses,exitEvent):
    controller = Controller(40)
    while True:
        # Get the command angle from the Consumer-Producers worker.
        # The minus off_center value will be control input for steering
        controller.main_processing(consumerbusses.read())

        # Move the robot
        controller.forward(20)

        # If exitEvent is true, stop the motor and while loop
        if exitEvent.is_set():
            controller.stop()
            break

        # Delay 0.1s
        time.sleep(0.1)

def ConsumerProducers(producebusses,consumerbusses,exitEvent):
    intpre = Interpretation(80,30)
    while True:
        # Get three sensor values from Producer worker.
        # Then, calculate the off-center and the direction
        intpre.graysensor_processing(producebusses.read())
        
        # Write the command angle on the Consumer busses.
        consumerbusses.write(-intpre.graysensor_output())

        # If exitEvent is true, stop the while loop
        if exitEvent.is_set():
            break
            
        # Delay 0.1s
        time.sleep(0.1)

def Producers(producebusses,exitEvent):
    sensor = Sensor()
    while True:
        # Read three sensor values.
        # Then, write the sensor values on the Producer busses.
        producebusses.write(sensor.graycolor.read())

        # If exitEvent is true, stop the while loop
        if exitEvent.is_set():
            break
            
        # Delay 0.1s
        time.sleep(0.1)

if __name__ == "__main__":
    producebusses = Busses()
    consumerbusses = Busses()
    exitEvent = threading.Event()  
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            eSensor = executor.submit(Producers,producebusses,exitEvent)
            eInterpreter = executor.submit(ConsumerProducers,producebusses,consumerbusses,exitEvent)
            eController = executor.submit(Consumers,consumerbusses,exitEvent)
    except KeyboardInterrupt:
        # If user type ctrl+c, send the event flag to all workers.
        print('Exit event')
        exitEvent.set()