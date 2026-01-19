from furnace import Furnace
import math
import matplotlib.pyplot as plt

Time = []
Fuzzy_temp = []

class Fuzzy:
    def __init__(self, furnace, ideal_temperature = 21):
        self.furnace = furnace
        self.ideal_temperature = ideal_temperature

    # Defining the different gaps using difference between ideal and current temperature.
    def large_gap(self, difference):
        if difference >= 6:
            return 1
        elif difference < 6 and difference > 4:
            return (difference - 4) / 2
        elif difference <= 4:
            return 0
        else:
            print("Error")
        
    def medium_gap(self, difference):
        if difference >= 6:
            return 0
        elif difference > 2 and difference < 4:
            return (difference - 2) / 2
        elif difference >= 4 and difference < 6:
            return (6 - difference) / 2
        elif difference <= 2:
            return 0
        else:
            print("Error")
        
    def small_gap(self, difference):
        if difference >= 4:
            return 0
        elif difference < 4 and difference > 2:
            return (4 - difference) / 2
        elif difference <= 2:
            return 1
        else:
            print("Error")

    def no_gap(self, difference):
        if difference <= 0.5:
            return 1
        if difference < 1:
            return (1 - difference) / 0.5
        else:
            return 0

    # The actual Fuzzy theory, we have the different values of the gaps and simply adding the numbers with their selective output and dividing by the denominator which is the 4 numbers summed (without the output)
    def process(self):
        self.difference = self.ideal_temperature - self.furnace.temperature

        none = self.no_gap(self.difference)
        small = self.small_gap(self.difference)
        medium = self.medium_gap(self.difference)
        large = self.large_gap(self.difference)

        # Playing around with these values may change the results drastically.
        No_Output = 0.30
        Low_Output = 0.40
        Medium_Output = 0.60
        High_Output = 0.90

        denom = none + small + medium + large

        power = ((none * No_Output) + (small * Low_Output) + (medium * Medium_Output) + (large * High_Output)) / denom if denom > 0 else 0

        self.furnace.step(power)

fuzzy = Fuzzy(Furnace(), ideal_temperature = 21)

def Fuzzy_run():
    for t in range (100):
        fuzzy.furnace.ambient = 12 + 4.0 * math.sin(2* math.pi * t / 24) # Makes a sin-wave out of the ambience temperature so it isn't constant. This program counts 1 rotation as an hour therefor this sin-wave accounts for night and day rotation.
        fuzzy.process()
        Time.append(t)
        Fuzzy_temp.append(fuzzy.furnace.temperature)
        print(f"Step {t}: {fuzzy.furnace.temperature:.2f}°C") #Prints the temperature with 2 decimals every hour.
