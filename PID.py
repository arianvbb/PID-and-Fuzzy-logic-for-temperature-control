from furnace import Furnace
import math
from rich.console import *
from rich.table import *

Time = []
PID_temp = []
PID_Energy_Usage = []
Within_1 = []

prev_difference = 21

class PID:
    def __init__(self, Kp = 2, Ki = 2.0, Kd = 0.5, furnace = None, ideal_temperature = 21):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.furnace = furnace
        self.ideal_temperature = ideal_temperature

        self.integral = 0.0
        self.prev_difference = 0.0

    def process(self, dt = 0.01):
        difference = self.ideal_temperature - self.furnace.temperature

        self.integral += difference * dt
        derivative = (difference - self.prev_difference) / dt

        power = self.Kp * difference + self.integral + self.Kd * derivative

        power = max(0.0, min(1.0, power))

        PID_Energy_Usage.append(power)

        self.furnace.step(power)

        self.prev_difference = difference

PID = PID(Kp = 1.5, Ki = 1.3, Kd = 0, furnace = Furnace())

def PID_run():

    warm_up = 15
    highest_temp = 21.1
    lowest_temp = 20.9

    for t in range (100):
        PID.furnace.ambient = 12 + 4.0 * math.sin(2* math.pi * t / 24) # Makes a sin-wave out of the ambience temperature so it isn't constant. This program counts 1 rotation as an hour therefor this sin-wave accounts for night and day rotation.
        PID.process()
        Time.append(t)
        PID_temp.append(PID.furnace.temperature)

        if t > warm_up:

            temp = PID.furnace.temperature

            if temp > highest_temp:
                highest_temp = temp
            elif temp < lowest_temp:
                lowest_temp = temp

            if 20 < temp < 22:
                Within_1.append(1)

    console = Console()

    table = Table(title = "PID")
    table.add_column("Metrics", style = "cyan")
    table.add_column("Data", style = "cyan")

    table.add_row("Average Output (%)", f"{((sum(PID_Energy_Usage)) / 100):.2f}")
    table.add_row("Within 1 degree (C)", f"{(sum(Within_1) / (100 - warm_up)):.2f}")
    table.add_row("Highest temp (C)", f"{highest_temp:.2f}")
    table.add_row("Lowest temp (C)", f"{lowest_temp:.2f}")

    console.print(table)
