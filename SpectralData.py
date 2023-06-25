import math 

class SpectrumDataPoint:
    def __init__(self, channel_name, wavelength, reading):
        self.channel_name = channel_name
        self.wavelength = wavelength
        self.reading = reading

class SpectroscopicData:
    def __init__(self, file_path):
        self.data_points = self.read_data(file_path)

    def read_data(self, file_path):
        data_points = []
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.split()
                channel_name = parts[0]
                wavelength = float(parts[1])
                reading = float(parts[3])
                data_point = SpectrumDataPoint(channel_name, wavelength, reading)
                data_points.append(data_point)
        return data_points

    def calculate_average(self, channel_name):
        readings = [data_point.reading for data_point in self.data_points if data_point.channel_name == channel_name]
        if readings:
            return sum(readings) / len(readings)
        else:
            return None

    def calculate_RMS(self, channel_name):
        readings = [data_point.reading for data_point in self.data_points if data_point.channel_name == channel_name]
        if readings:
            squared_diff = [(reading - self.calculate_average(channel_name)) ** 2 for reading in readings]
            mean_squared_diff = sum(squared_diff) / len(readings)
            return math.sqrt(mean_squared_diff)
        else:
            return None
