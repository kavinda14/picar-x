from adc import ADC

class Sensor():
    def __init__(self, ad0, adc1, adc2):
        self.adc0 = ad0
        self.adc1 = adc1
        self.adc2 = adc2
        self.poll_adc0, self.poll_adc1, self.poll_adc2 = [list() for _ in range(3)]

    def get_sensor_reading(self):
        adc_value_list = []
        adc_value_list.append(self.adc0.read())
        adc_value_list.append(self.adc1.read())
        adc_value_list.append(self.adc2.read())
        return adc_value_list

# if __name__ == "__main__":
