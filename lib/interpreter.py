
class Interpreter():
    def __init__(self, sensitivity=1000, polarity=10):
        self.sensitivity = sensitivity
        self.polarity = polarity

    def get_line_status(self, adc_value_list):
        if adc_value_list[0] > self.sensitivity and adc_value_list[1] > self.sensitivity and adc_value_list[2] > self.sensitivity:
            return 'stop'
            
        elif adc_value_list[1] <= self.sensitivity:
            return 'forward'
        
        elif adc_value_list[0] <= self.sensitivity:
            return 'right'

        elif adc_value_list[2] <= self.sensitivity:
            return 'left'
