from os import sendfile
from picarx import Picarx

class Controller(object):
    def __init__(self, scale = 40):
        super().__init__()
        self.scale = scale
        self.px = Picarx()

    def processing(self, control_value):
        # This method call the servo steering method
        # so that it turns the car toward the line
        cmd_value = control_value*self.scale
        self.px.set_dir_servo_angle(cmd_value)

        # It return the commanded steering angle
        return cmd_value

    def forward(self, forward_value):
        # This method call the motor forward command
        self.px.forward(forward_value)

# class Controller():
#     def __init__(self, picarx):
#         self.px = picarx
#         self.px_power = 10
#         self.interpreter = Interpreter()

#     def control_car(self, value_from_interpreter):
#         command = self.interpreter.get_line_status(value_from_interpreter)

#         if command == 'forward':
#             print(1)
#             self.px.forward(self.px_power) 

#         elif command == 'left':
#             self.px.set_dir_servo_angle(12)
#             self.px.forward(self.px_power) 

#         elif command == 'right':
#             self.px.set_dir_servo_angle(-12)
#             self.px.forward(self.px_power) 
#         else:
#             self.px.set_dir_servo_angle(0)
#             self.px.stop()