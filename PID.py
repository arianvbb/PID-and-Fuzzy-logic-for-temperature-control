from furnace import Furnace
import matplotlib.pyplot as plt
import math

Time = []
PID_temp = []

prev_difference = 21

class PID:
    def __init__(self, Kp = 2, Ki = 1.5, Kd = 0.5, furnace = None, ideal_temperature = 21):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.furnace = furnace
        self.ideal_temperature = ideal_temperature

    def process(self, dt = 0.01):

        global prev_difference

        difference = self.ideal_temperature - self.furnace.temperature

        power = self.Kp * difference + self.Ki * difference * dt + self.Kd * (difference - prev_difference) / dt

        self.furnace.step(power)

        prev_difference = difference

PID = PID(Kp = 1.5, Ki = 1.3, Kd = 0, furnace = Furnace())

def PID_run():    
    for t in range (100):
        PID.furnace.ambient = 12 + 4.0 * math.sin(2* math.pi * t / 24) # Makes a sin-wave out of the ambience temperature so it isn't constant. This program counts 1 rotation as an hour therefor this sin-wave accounts for night and day rotation.
        PID.process()
        Time.append(t)
        PID_temp.append(PID.furnace.temperature)
        print(f"Step {t}: {PID.furnace.temperature:.2f}°C") #Prints the temperature with 2 decimals every hour.
