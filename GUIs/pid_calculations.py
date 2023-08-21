"""
Simplistic system to roughly simulate a heater and PID controller.
This code was created simply to create a plot for use in the GUI demonstration
and should be very carefully examined and improved before use in any real
calculations.
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

"""
Heat is passed from a heater to an object.
The objects temperature is raised per the following

q = mass * specific heat * dT
dT = q / (mass * specific heat)

Now, the transfer of heat from heater to object is based on:

q = h * A * (T_heater - T_object)

Assume some heat loss in system.
"""


class Sample:
    """
    Simple object to be heated.  Uses
    q = c * m * dT
    where q = heat flux in J/sec
          c = specific heat in J/(kg*degC)
          m = mass in kg
          dT = change in temperature in degC
    """

    def __init__(self):
        # Generic choices for mass, specific heat, and initial temperature
        self.mass = 1.0  # kg
        self.specific_heat = 500.0  # J/(kg*degC)
        self.temperature = 25  # deg C

    def apply_heat(self, q: float, dt: float):
        """
        Args:
            q:  heat transfer rate in J/sec
            dt: time step in seconds
        """
        dT = dt * q / (self.mass * self.specific_heat)
        self.temperature += dT


def generate_PID_plot(kp: float, ki: float, kd: float):
    """ Generate a tk-compatible image of a plot that shows a specific
        PID response to a step change in temperature set point.

    Args:
        kp: Proportional Gain
        ki: Integral Gain
        kd: Differential Gain

    Returns:
        tk-compatible image

    """
    # create time arrays
    time_data = np.arange(0, 20, 0.05)

    # create target step function with target=25 if time<1 and target=200 if
    #   time >= 1
    target_data = np.heaviside(time_data-1, 1)
    target_data = 25 + 175*target_data

    # create array to hold the measured temperature of the sample to be heated
    value_data = np.zeros(time_data.shape)

    # create array to hold heater temperature, initialized to 25 degC
    heater_data = np.ones(time_data.shape) * 25.0

    # create sample to be heated
    sample = Sample()

    # initialize variables used in loop
    integral = 0.0
    prev_error = 0.0

    # generic heater variables
    h_heater = 1000.0  # J/(sec*m2)
    A_heater = 1.0  # m2

    # Loop for doing time calculations
    for i in range(len(time_data)-1):
        # Get time step information
        target = target_data[i]
        value = sample.temperature
        value_data[i] = value
        dt = time_data[i+1] - time_data[i]

        # PID calculations
        error = target - value
        integral = integral + error * dt
        velocity = kp * error + ki * integral + kd * (error - prev_error) / dt
        prev_error = error

        # Modify heater temperature based on PID response
        heater_data[i+1] = heater_data[i] + velocity * dt

        # Apply heat to the sample
        q = h_heater * A_heater * (heater_data[i+1] - sample.temperature)
        sample.apply_heat(q, dt)

    # Update the final samples temperature so that plot doesn't have a
    #  drop off to default value of 25
    value_data[-1] = value_data[-2]

    # Create plot that shows the target, sample, and heater temperatures
    #   vs. time
    fig, ax = plt.subplots()
    ax.plot(time_data, target_data)
    ax.plot(time_data, heater_data)
    ax.plot(time_data, value_data)
    ax.legend(["Target", "Heater", "Sample"])
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature")
    # Convert to a tk-compatible image
    canvas = fig.canvas
    canvas.draw()
    width, height = canvas.get_width_height()
    image_array = np.frombuffer(canvas.tostring_rgb(), dtype='uint8')
    image_array = image_array.reshape(height, width, 3)
    image = Image.fromarray(image_array)
    image_tk = ImageTk.PhotoImage(image)
    # plt.show()
    return image_tk


if __name__ == '__main__':
    generate_PID_plot(5, 0, 1)
