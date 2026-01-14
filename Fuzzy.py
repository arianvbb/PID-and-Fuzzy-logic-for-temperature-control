from main import Furnace
import math

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
        elif self.difference >= 4 and difference < 6:
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

    # The actual Fuzzy theory, we have the different values of the gaps and simply adding the numbers with their selective output and dividing by the denominator which is the 3 numbers summed (without the output)
    def process(self):
        self.difference = self.ideal_temperature - self.furnace.temperature

        small = self.small_gap(self.difference)
        medium = self.medium_gap(self.difference)
        large = self.large_gap(self.difference)

        Low_Output = 0.40
        Medium_Output = 0.50
        High_Output = 0.90

        denom = small + medium + large

        power = ((small * Low_Output) + (medium * Medium_Output) + (large * High_Output)) / denom if denom > 0 else 0

        self.furnace.step(power)

fuzzy = Fuzzy(Furnace(), ideal_temperature = 21)

for t in range (2000):
    fuzzy.furnace.ambient = 12 + 4.0 * math.sin(2* math.pi * t / 24) # Makes a sin-wave out of the ambience temperature so it isn't constant. This program counts 1 rotation as an hour therefor this sin-wave accounts for night and day rotation.
    fuzzy.process()
    print(f"Step {t}: {fuzzy.furnace.temperature:.2f}°C") #Prints the temperature with 2 decimals every hour.


        
    