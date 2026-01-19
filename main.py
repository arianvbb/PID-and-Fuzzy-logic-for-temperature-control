import random

class Furnace:
    def __init__(self, temperature = 0.0, ambient = None, heater_gain = 2.0, loss_coeff = 0.08): # Creating an instance with variable values.

        self.temperature = temperature
        self.ambient = ambient
        self.heater_gain = heater_gain
        self.loss_coeff = loss_coeff

    # This will run every time the temperature changes, it uses an ODE equation to calculate temperature gain based on the ambient temperature, loss_coefficient and the power given considering a 2,0 set heater_gain
    def step(self, power, ambient = None, dt = 1.0):
        if ambient is not None:
            self.ambient = ambient
        power = max(0.0, min(1.0, power))

        # Adding something that accounts for the door occasionally opening up.
        door = 1
        if random.random() < 0.02: # 2% Chance
            door = max(1.0, random.gauss(3, 0.5))
        else:
            door = 1

        dTdt = self.heater_gain * power - self.loss_coeff * door * (self.temperature - self.ambient)
        self.temperature += dTdt * dt

        return self.temperature
