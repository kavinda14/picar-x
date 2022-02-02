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