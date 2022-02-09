import sys

from week4 import ConsumerProducers

from rossros import *
from controller import Controller
from sensor import Sensor
from interpreter import Interpretation


def prodFunc():
    sensor = Sensor()
    # Read the ultrasonic sensor.
    return sensor.ultrasonic.read()

def consProdFunc(sensorValue):
    intpre = Interpretation()
    # Check if the sensor value is larger than threshold.
    return intpre.ultrasonic_processing(sensorValue)

def consFunc(CmdBool):
    ctrl = Controller()
    # Consumer Function makes the car moving or stop based on Interpreter.
    if CmdBool:
        ctrl.stop()
    else:
        ctrl.forward(20)

if __name__ == "__main__":
    prodBus = Bus()
    consBus = Bus()
    termBus = Bus()
    timer = Timer(termBus,5,0.1,termBus,"Timer")
    prod=Producer(prodFunc,prodBus,0.02,termBus,"")
    cons=Consumer(consFunc,consBus,0.05,termBus,"")
    prodcons = ConsumerProducer(consProdFunc,prodBus,consBus,0.1,termBus)

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        eSensor = executor.submit(prod)
        eInterpreter = executor.submit(prodcons)
        eController = executor.submit(cons)
        eTimer = executor.submit(timer)