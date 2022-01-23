from os import sendfile
from picarx import Picarx
from interpreter import Interpreter

class Controller():
    def __init__(self, picarx):
        self.px = picarx
        self.px_power = 10
        self.interpreter = Interpreter()

    def control_car(self, value_from_interpreter):
        command = self.interpreter.get_line_status(value_from_interpreter)

        if command == 'forward':
            print(1)
            self.px.forward(self.px_power) 

        elif command == 'left':
            self.px.set_dir_servo_angle(12)
            self.px.forward(self.px_power) 

        elif command == 'right':
            self.px.set_dir_servo_angle(-12)
            self.px.forward(self.px_power) 
        else:
            self.px.set_dir_servo_angle(0)
            self.px.stop()