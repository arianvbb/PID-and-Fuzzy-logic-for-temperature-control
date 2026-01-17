from main import Furnace
import matplotlib.pyplot as plt
import math

Time = []
Temperatures = []

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
    
for t in range (100):
    PID.furnace.ambient = 12 + 4.0 * math.sin(2* math.pi * t / 24) # Makes a sin-wave out of the ambience temperature so it isn't constant. This program counts 1 rotation as an hour therefor this sin-wave accounts for night and day rotation.
    PID.process()
    Time.append(t)
    Temperatures.append(PID.furnace.temperature)
    print(f"Step {t}: {PID.furnace.temperature:.2f}°C") #Prints the temperature with 2 decimals every hour.

# Plots the collected data.
plt.plot(Time, Temperatures)
plt.xlabel("Time (h)")
plt.ylabel("Temperatures (C)")
plt.axhline(21, color = 'red', label = "Ideal_temp")
plt.show()
