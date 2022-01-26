
class Interpreter():
    def __init__(self, sensitivity=80, polarity=30):
        self.sensitivity = sensitivity
        self.polarity = polarity

    def processing(self, value_list):
        # Redefine the sensor value for intuition
        left_value = value_list[0]
        center_value = value_list[1]
        right_value = value_list[2]
        # Tape is detected on the right side of robot.
        if right_value > self.sens and center_value <= self.sens:
            line_mag = (center_value+right_value)/2 - left_value
            # If the difference of sensor value is larger than the polarity,
            # store the values. If not, reset the values.
            if line_mag >= self.pol:
                self.line_dir = 1.0    
                self.line_mag = line_mag
            else:
                self.line_dir = 0.0
                self.line_mag = 0.0
        # Tape is detected on the left side of robot.
        elif left_value > self.sens and center_value <= self.sens:
            line_mag = (left_value+center_value)/2 - right_value
            # If the difference of sensor value is larger than the polarity,
            # store the values. If not, reset the values.
            if line_mag >= self.pol:
                self.line_dir = -1.0
                self.line_mag = line_mag
            else:
                self.line_dir = 0.0
                self.line_mag = 0.0  
        # Tape is detected on the center of robot.
        else:
            self.line_dir = 0.0
            self.line_mag = 0.0
        
    def output(self):
        return self.line_mag * self.line_dir / 250